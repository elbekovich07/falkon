from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.encoding import force_bytes

from app.forms import CustomerForm
from users.forms import RegisterModelForm, LoginForm
from users.models import Customer
from users.tokens import account_activation_token


# Create your views here.


class CustomerListView(ListView):
    model = Customer
    template_name = 'app/customers.html'
    context_object_name = 'customers'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Customer.objects.filter(name__icontains=query)
        return Customer.objects.all()


class CustomerDetailView(View):
    def get(self, request, slug):
        customer = get_object_or_404(Customer, slug=slug)
        return render(request, 'app/customer-details.html', {'customer': customer})


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'app/customer_add.html'
    success_url = reverse_lazy('users:customers')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'app/customer_update.html'
    success_url = reverse_lazy('users:customers')

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, name=self.kwargs.get('slug'))


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'app/customer_delete.html'
    success_url = reverse_lazy('users:customers')

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, slug=self.kwargs.get('slug'))


class LoginPage(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('app:index')
                else:
                    messages.error(request, 'Disabled account')
            else:
                messages.error(request, 'Username or Password invalid')

        return render(request, 'users/login.html', {'form': form})


class RegisterPage(CreateView):
    model = Customer
    form_class = RegisterModelForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        subject = 'Verify your email'
        message = render_to_string('users/Email/verify_email_message.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(subject, message, to=[user.email])
        email.content_subtype = 'html'
        email.send()

        messages.success(self.request, "Please check your email to complete registration.")
        return super().form_valid(form)


def email_required(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = request.user

        if user.is_authenticated and not user.is_active:
            user.email = email
            user.save()
            return redirect('app:index')
    return render(request, 'Github/email-required.html')


def verify_email_done(request):
    return render(request, 'users/Email/verify_email_done.html')


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Thank you for your email confirmation.')
        return redirect('app:index')
    else:
        messages.error(request, 'Activation link is invalid.')
    return render(request, 'users/Email/verify_email_confirm.html')



class LogoutView(View):
    def get(self, request):
        return render(request, 'users/logout.html')

    def post(self, request):
        logout(request)
        messages.success(request, "Succesfully logout")
        return redirect('app:index')
