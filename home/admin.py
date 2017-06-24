# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import Whatsup, Photowall


class PhotowallAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description')
    admin_thumbnail = AdminThumbnail(image_field='photo')

admin.site.register(Photowall, PhotowallAdmin)
admin.site.register(Whatsup)
admin.site.site_header = 'Wuga Admin System'
