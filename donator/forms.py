from django.core import validators
from django import forms

class SignupDonatorForm(forms.Form):
    FIRST_NAME = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your First Name'}))
    LAST_NAME = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Last Name'}))
    EMAIL = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email Address'}))
    CONTACT = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Contact Number'}))
    NID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your NID no.'}))
    PASSWORD = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
    CONFIRM_PASSWORD = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Your Password'}))


class LoginDonatorForm(forms.Form):
    EMAIL = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email Address'}))
    PASSWORD = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
