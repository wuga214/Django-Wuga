# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Profile(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^(\([0-9]{3}\)|[0-9]{3}-)[0-9]{3}-[0-9]{4}$',
                                 message="Need Valid Phone Number")
    phone = models.CharField(max_length=15, validators=[phone_regex], blank=True)
    address = models.CharField(max_length=200)
    photo = ProcessedImageField(blank=False,
                                      processors=[ResizeToFill(300, 400)],
                                      format='JPEG',
                                      options={'quality': 60})
    biography = MarkdownxField(blank=True)

    # Create a property that returns the markdown instead
    @property
    def formatted_biography(self):
        return markdownify(self.biography)

    def __str__(self):
        return self.name + ' - ' + self.email


class Publication(models.Model):
    PUBLICATION_CATEGORY = (
        ('AAAI', "Association for the Advancement of Artificial Intelligence (AAAI)"),
        ('NIPS', "Neural Information Processing Systems (NIPS)"),
        ('IJCAI', "International Joint Conference on Artificial Intelligence (IJCAI)"),
        ('ICML', "International Conference on Machine Learning (ICML)"),
        ('ARXIV', "ArXiv- Waiting to Publish")
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    time = models.DateField()
    coauthors = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=10, choices=PUBLICATION_CATEGORY, default='AAAI')
    paper_link = models.CharField(max_length=200)
    code_link = models.CharField(max_length=200, blank=True)
    presentation_link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
