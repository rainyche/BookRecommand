from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    keywords = forms.CharField(max_length=200)
    subjects = forms.CharField(max_length=200)
    industry = forms.CharField(max_length=200)
    major = forms.CharField(max_length=200)
    books = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','keywords','subjects','industry','major','books')

