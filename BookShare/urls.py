from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^$', views.welcome, name='welcome'), # welcome page where user can go to sign up page
               url(r'^signup', views.signup, name='signup'), # sign up page
               url(r'^home', views.home, name='home'), # home page after sign up
               url(r'^user_profile', views.eachuser, name='eachuser'), # display the user's profile
               url(r'^display_book', views.recommendations, name='recommendations'), # display books recommended for the user
]
