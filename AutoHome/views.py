# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic

# TODO get the views ready

# TODO check the login view


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Successfully logged in.')
        else:
            return HttpResponse('No such user exists')
    else:
        return HttpResponseRedirect(reverse('AutoHome:index'))

# TODO check the register view


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponse('signed up successfully')
    else:
        form = UserCreationForm()
    return render(request, 'AutoHome/signup.html', {'form': form})

# TODO finish up rest of the views


def index(request):
    return render(request, 'AutoHome/index.html')


def settings(request):
    return


class StatusView(generic.ListView):
    pass

    def get_queryset(self):
        """ Return list of devices """
        return


class ControlView(generic.DetailView):
    pass

