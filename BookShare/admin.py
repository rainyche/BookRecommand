# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from BookShare.models import user
from BookShare.models import Book

# Register your models here.
admin.site.register(user)
admin.site.register(Book)
