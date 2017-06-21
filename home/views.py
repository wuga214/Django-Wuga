# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.shortcuts import render,get_object_or_404
from django.utils.datetime_safe import datetime

from .models import Whatsup, Photowall


def indexview(request):
    range_start = datetime.now() - timedelta(days=100)
    photos = Photowall.objects.filter(time__gte=range_start)
    news = Whatsup.objects.filter(time__gte=range_start)
    context = {
        "photos": photos,
        "news": news
    }
    return render(request, 'home/index.html', context)

