# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.shortcuts import render
from django.utils.datetime_safe import datetime

from .models import Whatsup, Photowall


def indexview(request):
    range_start = datetime.now() - timedelta(days=100)
    photos = Photowall.objects.filter(time__gte=range_start).order_by('-time')
    news = Whatsup.objects.filter(time__gte=range_start).order_by('-time')
    context = {
        "photos": photos,
        "news": news
    }
    return render(request, 'home/index.html', context)

