import logging

from asgiref.sync import iscoroutinefunction
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import sync_and_async_middleware
from django.utils.timezone import now


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Request send")

    def __call__(self, request):
        print("Request received")
        response = self.get_response(request)
        print("Response returned")
        return response

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Request Method: {request.method}, Request Path: {request.path}")
        response = self.get_response(request)
        return response


class AutoLogoutMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activiy')
            if last_activity is not None:
                difference_time = (now() - now().fromisoformat(last_activity)).total_seconds()
                if difference_time > settings.SESSION_COOKIE_AGE:
                    logout(request)
                    return redirect('app:index')

            request.session['last_activity'] = now().isoformat()

        response = self.get_response(request)
        return response


logger = logging.getLogger(__name__)

MOBILE_KEYWORDS = ['Mobile', 'Android', 'iPhone', 'iPad']


@sync_and_async_middleware
def user_agent_detection_middleware(get_response):
    def detect_device(user_agent):
        if user_agent:
            for keyword in MOBILE_KEYWORDS:
                if keyword.lower() in user_agent.lower():
                    return "Mobile"
        return "Desktop"

    if iscoroutinefunction(get_response):
        async def middleware(request):
            user_agent = request.META.get('HTTP_USER_AGENT', "")
            device_type = detect_device(user_agent)
            request.device_type = device_type
            print(f"[ASYNC] {request.method} {request.path} | Device: {device_type} | UA: {user_agent}")
            return await get_response(request)
    else:
        def middleware(request):
            user_agent = request.META.get('HTTP_USER_AGENT', "")
            device_type = detect_device(user_agent)
            request.device_type = device_type
            print(f"[SYNC] {request.method} {request.path} | Device: {device_type} | UA: {user_agent}")
            return get_response(request)

    return middleware


class SecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        referer = request.META.get('HTTP_REFERER', "")
        if not referer:
            return HttpResponse("For security reasons, this request cannot be accepted.")

        response = self.get_response(request)
        return response

