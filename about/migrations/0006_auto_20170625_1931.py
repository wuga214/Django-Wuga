# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20170625_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='coauthers',
            new_name='coauthors',
        ),
    ]
