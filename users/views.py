from django.shortcuts import render

from users.models import CustomUser
from .forms import CustomerForm



# Create your views here.

def customer_list(request):
    query = request.GET.get('q', '')
    customers = CustomUser.objects.all()

    if query:
        customers = customers.filter(name__icontains=query)

    return render(request, 'users/customers.html', {'customers': customers, 'query': query})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/customers.html', {'form': form})
        else:
            form = CustomerForm()
        return render(request, 'users/customers.html', {'form': form})
