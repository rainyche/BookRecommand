# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django

# Create your models here.
# class UserProfile(models.Model):
#     name = models.ForeignKey('auth.User')
#     email = models.CharField(max_length=200)
#     keywords = models.TextField()
#     subjects = models.CharField(max_length=200)
#     industry = models.CharField(max_length=200)
#     major = models.CharField(max_length=200)
#     books = models.ManyToManyField(Book)

#     def save(self):
#         self.save()

#     def __str__(self):
#         return self.name




class Uuser(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    keywords = models.TextField()
    subjects = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    books = models.CharField(max_length=200)

    def __str__(self):
        return self.name
