# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 03:03
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_auto_20170620_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_logo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=b''),
        ),
    ]