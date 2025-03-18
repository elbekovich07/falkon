from django.urls import path

from app import views
from app.views import customer_view, customer_detail, customer_create, customer_update, customer_delete

urlpatterns = [

    path('', views.index, name='index'),
    path('products_list/<int:category_id>', views.index, name='products_list_by_category'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('customers/', customer_view, name='customers'),
    path('customers/<int:pk>/', customer_detail, name='customer_detail'),
    path('customers/new/', customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', customer_delete, name='customer_delete'),
]
