# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_domain_domain_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_logo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
