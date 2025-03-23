from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app.forms import CustomerForm
from users.forms import RegisterModelForm, LoginForm
from users.models import Customer


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


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'app/customer-details.html'
    context_object_name = 'customer'

    def get_object(self, queryset=None):
        return get_object_or_404(Customer, name=self.kwargs.get('slug'))



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


class RegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = RegisterModelForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(user.password)
        user.save()
        send_mail(
            'Helllo Dear!',
            'You are successfully registered!',
            'olmosnormuminov02@gmail.com',
            [user.email],
            fail_silently=False,
        )
        login(self.request, user)
        return redirect('app:index')


class LogoutView(View):
    def get(self, request):
        return render(request, 'users/logout.html')

    def post(self, request):
        logout(request)
        return redirect('shop:index')
