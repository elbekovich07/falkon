from django.urls import path, include


from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('products_list/<int:category_id>', views.index, name='product_list'),
    path('customers/', views.customers_view, name='customers'),
]
