# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


# TODO check if the database is appropriate to the problem we're solving (i.e. AutoHome)


class Timer(models.Model):
    from_time = models.DateTimeField(null=True)
    to_time = models.DateTimeField(null=True)

    def calculate_time(self):
        return self.to_time - self.from_time

    def set_time(self, from_time, to_time):
        self.from_time = from_time
        self.to_time = to_time

    def get_time(self):
        return  str(self.from_time) + ' - ' + str(self.to_time)

    def __str__(self):
        return self.get_time()


class Room(models.Model):
    _name = models.CharField(verbose_name='Name of the room', max_length=256)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self._name


class Device(models.Model):
    modified = models.DateTimeField()
    dev_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    dev_power = models.BooleanField('Device power')
    dev_timer = models.OneToOneField(Timer, on_delete=models.CASCADE)
    dev_name = models.CharField(verbose_name='Name of device', max_length=256)

    @property
    def modification_time(self):
        return self.modified

    @modification_time.setter
    def modification_time(self, value):
        self.modified = value

    @property
    def room(self):
        return self.dev_room.name

    @room.setter
    def room(self, name):
        self.dev_room.name = name

    @property
    def power(self):
        return self.dev_power

    @power.setter
    def power(self, new_power):
        self.dev_power = new_power

    @property
    def timer(self):
        return self.dev_timer.get_time()

    @timer.setter
    def timer(self, time):
        self.dev_timer.set_time(time[0], time[1])

    @property
    def name(self):
        return self.dev_name

    @name.setter
    def name(self, new_name):
        self.dev_name = new_name

    def __str__(self):
        return self.dev_name + ' in the ' + self.dev_room.name


# TODO test profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_accessed = models.DateTimeField(null=True)
    device = models.ManyToManyField(Device)

    def __str__(self):
        return self.user.username

# TODO test sensor


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
