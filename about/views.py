# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Profile


def indexview(request):
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles,
    }
    return render(request, 'about/index.html', context)