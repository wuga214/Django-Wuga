# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Publication
from imagekit.admin import AdminThumbnail
from markdownx.admin import MarkdownxModelAdmin


class ProfileAdmin(MarkdownxModelAdmin):
    list_display = ('__str__', 'name')
    admin_thumbnail = AdminThumbnail(image_field='photo')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Publication)