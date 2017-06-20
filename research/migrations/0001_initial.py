# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 00:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_type', models.CharField(choices=[('DL', 'Deep Learning'), ('PGM', 'Probabilistic Graphical Model'), ('CO', 'Convex Optimization'), ('RD', 'Random Exploration')], default='RD', max_length=3)),
                ('project_short_description', models.CharField(max_length=200)),
                ('project_long_description', markdownx.models.MarkdownxField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.Domain')),
            ],
        ),
    ]
