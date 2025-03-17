from django.urls import path, include


from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/<int:category_id>', views.index, name='product_list'),
    # path('products/category/<int:category_id>/', product_list, name='product-by-category'),
    # path('products/<int:product_id>/', product_detail, name='product-detail'),
]
