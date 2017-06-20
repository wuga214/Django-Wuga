# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from markdownx.models import MarkdownxField


class Domain(models.Model):
    domain_name = models.CharField(max_length=100)

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


