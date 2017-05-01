# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django

# This is the user class. Each user has a name, email address, keywords that 
# he/she is interested in, subjects he/she is interested in, industry he/she 
# is working in, his/her major, and the books that he/she recommend to others.

class Uuser(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    keywords = models.TextField()
    subjects = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    books = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add = True, editable=False)
    
    class Meta:
        get_latest_by = 'creation_date'

    def __str__(self):
        return self.name
