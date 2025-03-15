from django import forms
from phonenumber_field.formfields import PhoneNumberField

from app.models import Product, Comment, Order, ProductImage


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image',]

ProductImageForm = forms.inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=5)


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('product',)


class OrderModelForm(forms.ModelForm):
    phone = PhoneNumberField(region='UZ')

    class Meta:
        model = Order
        exclude = ('product',)