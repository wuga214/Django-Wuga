# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_publications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publications',
            new_name='Publication',
        ),
    ]
