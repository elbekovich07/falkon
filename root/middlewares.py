from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
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
