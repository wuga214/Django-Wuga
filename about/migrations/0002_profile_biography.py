# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 17:46
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
    ]
