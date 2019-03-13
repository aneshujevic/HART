# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.views import generic

from django.utils import timezone

# TODO get the views ready


def login(request):
    return

# TODO test timezone


def index(request):
    HttpResponse(timezone.now())


def settings(request):
    return


class StatusView(generic.ListView):
    pass

    def get_queryset(self):
        """ Return list of devices """
        return



class ControlView(generic.DetailView):
    pass

