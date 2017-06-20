# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from markdownx.models import MarkdownxField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Domain(models.Model):
    domain_name = models.CharField(max_length=100)
    domain_logo = ProcessedImageField(blank=True,
                                      processors=[ResizeToFill(100, 200)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return self.domain_name


class Project(models.Model):
    PROJECT_CATEGORY = (
        ('DL', "Deep Learning"),
        ('PGM', "Probabilistic Graphical Model"),
        ('CO', "Convex Optimization"),
        ('RD', "Random Exploration"),
    )
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=3, choices=PROJECT_CATEGORY, default='RD')
    project_short_description = models.CharField(max_length=200)
    project_long_description = MarkdownxField()

    def __str__(self):
        return self.project_name


