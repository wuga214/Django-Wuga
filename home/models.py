# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.datetime_safe import datetime
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class Whatsup(models.Model):
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    time = models.DateField()

    def __str__(self):
        return self.description


class Photowall(models.Model):
    location = models.CharField(max_length=100)
    time = models.DateField()
    description = models.CharField(max_length=200)
    photo = ProcessedImageField(blank=True,
                                processors=[ResizeToFill(1170, 450)],
                                format='JPEG',
                                options={'quality': 72})

    def __str__(self):
        return self.description + " - " + self.location + " - " + str(self.time)
