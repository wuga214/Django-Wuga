# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_profile_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.DateField()),
                ('publisher', models.CharField(choices=[('AAAI', 'Association for the Advancement of Artificial Intelligence (AAAI)'), ('NIPS', 'Neural Information Processing Systems (NIPS)'), ('IJCAI', 'International Joint Conference on Artificial Intelligence (IJCAI)'), ('ICML', 'International Conference on Machine Learning (ICML)')], default='AAAI', max_length=10)),
                ('paper_link', models.CharField(max_length=200)),
                ('code_link', models.CharField(max_length=200)),
                ('presentation_link', models.CharField(blank=True, max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.Profile')),
            ],
        ),
    ]
