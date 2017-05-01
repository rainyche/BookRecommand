#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from BookShare.forms import SignUpForm
from BookShare.recommendation import recommend
from BookShare.models import Uuser

# process the sign up page
def signup(request):

    # if a form is submitted
    if request.method == "POST":
        form = SignUpForm(request.POST)

        # check whether the form is valid or not
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  

            # load the profile instance created by the signal
            user.email = form.cleaned_data.get('email')
            user.keywords = form.cleaned_data.get('keywords')
            user.subjects = form.cleaned_data.get('subjects')
            user.industry = form.cleaned_data.get('industry')
            user.major = form.cleaned_data.get('major')
            user.books = form.cleaned_data.get('books')
            user.save()

        # then go to the home page
        return redirect('home')
    else:

        # else reder the form again
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


# render the home page
def home(request):
    return render(request, 'BookShare/home.html')

# render the welcome page
def welcome(request):
    return render(request, 'BookShare/welcome.html')

# render the user-profile page
def eachuser(request):
    thisuser = Uuser.objects.latest()
    return render(request, 'BookShare/user_profile.html', {"user" : thisuser})

# apply the recommendation function on current user and display books recommended
def recommendations(request):
    thisuser = Uuser.objects.latest()
    booklist = recommend(thisuser)
    return render(request, 'BookShare/display_book.html', {"books" : booklist})
