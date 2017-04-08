# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookShare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reviewers',
        ),
        migrations.AlterField(
            model_name='user',
            name='books',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]