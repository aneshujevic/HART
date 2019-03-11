# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# TODO test models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_accessed = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username


class Timer(models.Model):
    from_time = models.DateTimeField(null=True)
    to_time = models.DateTimeField(null=True)

    def calculate_time(self):
        return self.to_time - self.from_time


class Room(models.Model):
    name = models.CharField(verbose_name='Name of the room', max_length=256)

    def __str__(self):
        return self.name


class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    power = models.BooleanField('Device power')
    timer = models.OneToOneField(Timer, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name of device', max_length='256')
    lats_time_modified = models.DateTimeField(null=True)
    user = models.ForeignKey(Profile)

    def __str__(self):
        return self.name + ' in the ' + self.room.name


class Sensor(models.Model):
    alarm_value = models.IntegerField(default=50)
    value = models.FloatField(default=0)
    name = models.CharField(max_length=256)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' in ' + self.room.name + ' has value' + str(self.value)

# TODO list of devices to be done


class DeviceList(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)

