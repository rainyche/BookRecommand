from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^$', views.welcome, name='welcome'),
               url(r'^user_profile', views.eachuser, name='eachuser'),
               url(r'^display_book', views.recommendations, name='recommendations'),
               url(r'^signup', views.signup, name='signup'),
               url(r'^home', views.home, name='home'),
]
