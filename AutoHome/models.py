# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from datetime import datetime
# TODO check if the database is appropriate to the problem we're solving (i.e. AutoHome)


# TODO check other functions of Timer


class Timer(models.Model):
    from_time = models.DateTimeField(null=True)
    to_time = models.DateTimeField(null=True)

    def calculate_time(self):
        return self.to_time - self.from_time

    def set_time(self, from_time, to_time):
        self.from_time = from_time
        self.to_time = to_time

    def get_time(self):
        return 'from ' + str(self.from_time) + ' to ' + str(self.to_time)

    def __str__(self):
        return self.get_time()


class Room(models.Model):
    name = models.CharField(verbose_name='Name of the room', max_length=256)

    def __str__(self):
        return self.name

# TODO test device


class Device(models.Model):
    modified = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    power = models.BooleanField('Device power')
    timer = models.OneToOneField(Timer, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name of device', max_length=256)

    def __str__(self):
        return self.name + ' in the ' + self.room.name


# TODO test device and sensor model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_accessed = models.DateTimeField(null=True)
    device = models.ManyToManyField(Device)

    def __str__(self):
        return self.user.username


class Sensor(models.Model):
    value = models.FloatField(default=0)
    name = models.CharField(max_length=256)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' in ' + self.room.name + ' has value' + str(self.value)

# TODO list of devices to be done


class DeviceList(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    from_to_time = models.OneToOneField(Timer, on_delete=models.CASCADE)

    def __str__(self):
        return self.device.name + 'is scheduled ' + self.from_to_time.get_time()

# TODO test sensor list

class SensorList(models.Model):
    alarm_value = models.IntegerField(default=50)
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE)
