from django.shortcuts import render, get_object_or_404, redirect

from .forms import CategoryModelForm

from .models import Category, Product

from django.core.paginator import Paginator


# Create your views here.


def index(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)

        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'categories': categories,
            'products': page_obj,
        }
        return render(request, 'app/product-list.html', context)
    context = {'categories': categories}
    return render(request, 'app/index.html', context)


def customers_view(request):
    return render(request, 'users/customers.html')
