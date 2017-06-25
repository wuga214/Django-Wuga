# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Paper(models.Model):
    PAPER_CATEGORY = (
        ('ST', "Something"),
    )
    title = models.CharField(max_length=100)
    time = models.DateField()
    category = models.CharField(max_length=3, choices=PAPER_CATEGORY, default='DL')
    abstract = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class WebPage(models.Model):
    PAGE_CATEGORY = (
        ('ST', "Something"),
    )
    PAGE_TYPE = (
        ('TT', "Tutorial"),
        ('DM', "DEMO"),
        ('NS', "NEWS"),
    )
    about = models.CharField(max_length=100)
    time = models.DateField()
    category = models.CharField(max_length=3, choices=PAGE_CATEGORY, default='DL')
    type = models.CharField(max_length=3, choices=PAGE_TYPE, default='DL')
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.about
