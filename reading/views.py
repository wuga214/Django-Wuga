# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Paper, WebPage


def indexview(request):
    papers = Paper.objects.all().order_by('time')[:5]
    webpages = WebPage.objects.all().order_by('time')[:5]
    categories = Paper.PAPER_CATEGORY
    selected_category = None
    context = {
        "papers": papers,
        "webpages": webpages,
        "categories": categories,
        "selected_category": selected_category,
    }
    return render(request, 'reading/index.html', context)


def filteredindexview(request, selected_category):
    papers = Paper.objects.filter(category=selected_category).order_by('time')[:5]
    webpages = WebPage.objects.filter(category=selected_category).order_by('time')[:5]
    categories = Paper.PAPER_CATEGORY
    context = {
        "papers": papers,
        "webpages": webpages,
        "categories": categories,
        "selected_category": selected_category,
    }
    return render(request, 'reading/index.html', context)
