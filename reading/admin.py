# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Paper, WebPage


admin.site.register(Paper)
admin.site.register(WebPage)