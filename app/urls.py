from django.urls import path

from app.views import IndexView, ProductDetailView, ProductListView
from users.views import (
    CustomerListView, CustomerDetailView,
    CustomerCreateView, CustomerUpdateView, CustomerDeleteView
)

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products_list/<slug:category_slug>/', ProductListView.as_view(), name='products_list_by_category'),
]
