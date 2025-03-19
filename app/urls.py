from django.urls import path

from app import views
from app.views import (
IndexView, ProductDetailView,
    CustomerListView, CustomerDetailView,
    CustomerCreateView, CustomerUpdateView, CustomerDeleteView
)

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('products_list/<int:category_id>', IndexView.as_view(), name='products_list_by_category'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/new/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:customer_id>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]
