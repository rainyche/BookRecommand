# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from BookShare.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Create your views here.
def homepage(request):
    return render(request, 'BookShare/home.html', {})

def eachuser(request, pk):
    user = UserProfile.objects.filter(id = pk)
    return render(request, 'BookShare/user_profile.html', {"user" : user})

def eachbook(request, pk):
    book = Book.objects.filter(id = pk)
    return render(request, 'BookShare/review.html', {"book" : book})

def recommendations(request, pk):
    user = UserProfile.objects.filter(id = pk)
    booklist = recommendation.recommend(user, Book)
    return render(request, 'BookShare/display_book.html', {"books" : booklist})
