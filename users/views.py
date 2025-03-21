from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from root import settings
from users.forms import RegisterModelForm


# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('shop:index')
            else:
                messages.error(request, 'Disabled account')
        else:
            messages.error(request, 'Username or Password invalid')

        return render(request, 'users/login.html')

class RegisterView(View):
    template_name = 'users/register.html'
    form_class = RegisterModelForm
    success_url = 'app:index'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(form.cleaned_data['password'])
        user.save()


        send_mail(
            subject='Hello Dear!',
            message='You successfully registered!',
            from_email='olmosnormuminov02@gmail.com',
            recipient_list=[user.email],
            fail_silently=False,
        )

        login(self.request, user)
        messages.success(self.request, 'You successfully registered!')

        return redirect(self.success_url)



class LogoutView(View):
    def get(self, request):
        return render(request, 'users/logout.html')

    def post(self, request):
        logout(request)
        return redirect('app:index')
