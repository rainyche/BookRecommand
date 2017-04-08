# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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
    booklist = recommendations.recommend(user, Book)
    return render(request, 'BookShare/display_book.html', {"books" : booklist})
