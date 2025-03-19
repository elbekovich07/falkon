from django import forms

from app.models import Product, Category, Customer


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['title']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'Billing_Address', 'image']

    image = forms.ImageField(required=False)