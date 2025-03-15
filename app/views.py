from django.shortcuts import render, get_object_or_404, redirect

from .forms import CategoryModelForm

from .models import Category, Product


# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)[:10]
    return render(request, 'app/index.html', {'categories': categories, 'products': products})


def product_list(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, is_active=True)
    else:
        products = Product.objects.filter(is_active=True)

    return render(request, 'app/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'app/product.html', {'product': product})

