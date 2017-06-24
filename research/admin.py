# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from imagekit.admin import AdminThumbnail
from .models import Domain, Project


class DomainAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'domain_name')
    admin_thumbnail = AdminThumbnail(image_field='domain_logo')

admin.site.register(Domain, DomainAdmin)
admin.site.register(Project, MarkdownxModelAdmin)
