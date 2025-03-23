from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

from users.apps import UsersConfig
from users.models import Customer



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput)



class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email', 'password', 'confirm_password')

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(f'This {email} already registered.')
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError(f'Password don\'t match')
        return confirm_password