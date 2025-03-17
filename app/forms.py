from django import forms

from app.models import Product, Category


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
