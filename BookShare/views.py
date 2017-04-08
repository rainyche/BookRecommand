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
            bookstr = get('books')
            bookattrlist = bookstr.split(",")
            user.books = Book(title = bookattrlist[0], author = bookattrlist[1], subjects = bookattrlist[2], review = bookattrlist[3], reviewers = user)

            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Create your views here.

def home(request):
    return render(request, 'BookShare/home.html')

def welcome(request):
    return render(request, 'BookShare/welcome.html')

def eachuser(request, id):
    user = UserProfile.objects.filter(id = id)
    return render(request, 'BookShare/user_profile.html', {"user" : user})

def eachbook(request, id):
    book = Book.objects.filter(id = id)
    return render(request, 'BookShare/review.html', {"book" : book})

def recommendations(request, id):
    user = UserProfile.objects.filter(id = id)
    booklist = recommendation.recommend(user, Book)
    return render(request, 'BookShare/display_book.html', {"books" : booklist})
