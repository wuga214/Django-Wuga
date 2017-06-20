# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Domain, Project


class IndexView(generic.ListView):
    template_name = 'research/index.html'
    context_object_name = 'domain_list'

    def get_queryset(self):
        """Return all domains"""
        return Domain.objects.all()


class DomainView(generic.DetailView):
    model = Domain
    template_name = 'research/domain.html'


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'research/detail.html'
