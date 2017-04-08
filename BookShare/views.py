#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from BookShare.forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.email = form.cleaned_data.get('email')
            user.keywords = form.cleaned_data.get('keywords')
            user.subjects = form.cleaned_data.get('subjects')
            user.industry = form.cleaned_data.get('industry')
            user.major = form.cleaned_data.get('major')
            user.books = form.cleaned_data.get('books')
            user.save()
        return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

# Create your views here.

def home(request):
    return render(request, 'BookShare/home.html')

def welcome(request):
    return render(request, 'BookShare/welcome.html')

def eachuser(request):
    user = request.user
    return render(request, 'BookShare/user_profile.html', {"user" : user})

def recommendations(request, id):
    user = user.objects.filter(id = id)
    booklist = recommendation.recommend(user)
    return render(request, 'BookShare/display_book.html', {"books" : booklist})
