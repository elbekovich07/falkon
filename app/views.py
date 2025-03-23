from django.db.models import Q
from django.views.generic import ListView, DetailView

from app.models import Category, Product


class IndexView(ListView):
    model = Product
    template_name = 'app/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            context['products'] = Product.objects.filter(category__slug=category_slug)

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product-detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return Product.objects.get(slug=self.kwargs.get('slug'))


class ProductListView(ListView):
    model = Product
    template_name = 'app/product-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            return Product.objects.filter(category__slug=category_slug)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

