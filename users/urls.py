from django.urls import path


from app import views

app_name = 'users'

urlpatterns = [
    path('customers/', views.customers_view, name='customers'),
    path('customers/<int:pk>/', views.customers_view, name='customers'),
    path('customers/add/', views.customers_view, name='customers-add'),
]
