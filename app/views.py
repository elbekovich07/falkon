from django.shortcuts import render, get_object_or_404, redirect

from app.forms import CustomerForm
from app.models import Category, Product, Customer


# Create your views here.


def index(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id:
        products = Product.objects.filter(category=category_id)
        context = {'products': products}
        return render(request, 'app/product-list.html', context)
    context = {'categories': categories, 'products': products}
    return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'app/product-detail.html', context)


def customer_view(request):
    customer = Customer.objects.all()
    return render(request, 'app/customers.html',{'customers': customer})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'app/customers.html', {'customer': customer})

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'app/customers.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'app/customers.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customer_list')
    return render(request, 'app/customers.html', {'customer': customer})