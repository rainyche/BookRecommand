from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^$', views.homepage, name='homepage'),
               url(r'^eachuser/(\d+)/$', views.eachuser, name='eachuser'),
               url(r'^eachbook/(\d+)/$', views.eachbook, name='eachbook'),
               url(r'^eachuser/recommendations/(\d+)/$', views.recommendations, name='recommendations'),
]
