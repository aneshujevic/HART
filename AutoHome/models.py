# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


# TODO check if the database is appropriate to the problem we're solving (i.e. AutoHome)

# TODO weak entity timer
class Timer(models.Model):
    from_time = models.DateTimeField(null=True)
    to_time = models.DateTimeField(null=True)

    def calculate_time(self):
        return self.to_time - self.from_time

    def set_time(self, from_time, to_time):
        self.from_time = from_time
        self.to_time = to_time

    def get_time(self):
        return str(self.from_time) + ' - ' + str(self.to_time)

    def __str__(self):
        return self.get_time()

# TODO check if the room with the same name exists


class Room(models.Model):
    _name = models.CharField(verbose_name='Name of the room', max_length=256, primary_key=True)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self._name


# TODO change room

class Device(models.Model):
    modified = models.DateTimeField(null=True)
    dev_room = models.ForeignKey(Room, on_delete=models.CASCADE, primary_key=True)
    dev_power = models.BooleanField('Device power')
    dev_timer = models.OneToOneField(Timer, on_delete=models.CASCADE)
    dev_name = models.CharField(verbose_name='Name of device', max_length=256, primary_key=True)

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


# TODO test profile, USER has permissions for certain devices


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_name = models.TextField(null=True)

    def change_pass(self, new_password):
        self.user.set_password(new_password)

    @property
    def f_name(self):
        return self.user.first_name

    @f_name.setter
    def f_name(self, value):
        self.user.first_name = value

    @property
    def l_name(self):
        return self.last_name

    @l_name.setter
    def l_name(self,value):
        self.last_name = value

    def __str__(self):
        return self.user.username

# TODO test sensor
# TODO change_room change


class Sensor(models.Model):
    _value = models.FloatField(default=0)
    alarm_value = models.IntegerField(default=50)
    _name = models.CharField(max_length=256, primary_key=True)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, primary_key=True)

    @property
    def value(self):
        return self._value

    @property
    def alarm(self):
        return self.alarm_value

    @alarm.setter
    def alarm(self, value):
        self.alarm_value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self.name + ' in ' + self.room.name + ' has value' + str(self.value)
