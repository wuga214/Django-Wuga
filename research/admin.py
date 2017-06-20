# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Domain, Project


admin.site.register(Domain)
admin.site.register(Project, MarkdownxModelAdmin)
