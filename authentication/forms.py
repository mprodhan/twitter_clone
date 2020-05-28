from django import forms
from django.contrib.auth.models import User
from authentication.models import user

class LoginForm(forms.Form):
    user = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)