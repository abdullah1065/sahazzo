from django.core import validators
from django import forms

class LoginAdminForm(forms.Form):
    EMAIL = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email Address'}))
    PASSWORD = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
