# BookRecommend URL Configuration

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    
    # admin page
    url(r'^admin/', admin.site.urls),

    # home page
    url(r'', include('BookShare.urls')),

    # logout page
    url(r'^logout/$', auth_views.logout, name = 'logout', kwargs={'next_page':'/'}),

    #login page
    url(r'^login/$', auth_views.login),
    ]
