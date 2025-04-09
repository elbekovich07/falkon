from django.urls import path

from users import views
from users.views import (
    CustomerListView, CustomerDetailView,
    CustomerCreateView, CustomerUpdateView, CustomerDeleteView
)

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('customers/new/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<slug:slug>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<slug:slug>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<slug:slug>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('email-required/', views.email_required, name='email_required'),
    path('verifiy-email-done/', views.verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify_email_confirm'),
    path('export-data/', views.export_data, name='export_data')
]
