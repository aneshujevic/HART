# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from django.views import generic

# TODO get the views ready


def login(request):
    pass


def index(request):
    pass


def settings(request):
    pass


class StatusView(generic.ListView):

    def get_queryset(self):
        """ Return list of devices """
        return
    pass


class ControlView(generic.DetailView):
    pass
