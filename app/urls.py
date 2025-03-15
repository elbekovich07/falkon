from django.urls import path
from app.views import index, product_list, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product-list'),
    path('products/category/<int:category_id>/', product_list, name='product-by-category'),
    path('products/<int:product_id>/', product_detail, name='product-detail'),
]
