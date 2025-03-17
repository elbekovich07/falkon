from django.shortcuts import render, get_object_or_404, redirect

from .forms import CategoryModelForm

from .models import Category, Product


# Create your views here.


def index(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context = {
            'categories': categories,
            'products': products,
        }
        return render(request, 'app/product_list.html', context)
    context = {'categories': categories}
    return render(request, 'app/index.html', context)


def products_of_category(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        context = {
            'products': products,
        }
        return render(request, 'app/product_list.html', context)
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     return render(request, 'app/product.html', {'product': product})
