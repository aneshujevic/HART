# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


# TODO check if the database is appropriate to the problem we're solving (i.e. AutoHome)


class Timer(models.Model):
    _from_time = models.DateTimeField(verbose_name='Scheduled from time', null=True)
    _to_time = models.DateTimeField(verbose_name='Scheduled to time', null=True)

    @property
    def to_time(self):
        return self._from_time

    @to_time.setter
    def to_time(self, new_to_time):
        self._to_time = new_to_time

    @property
    def from_time(self):
        return self._from_time

    @from_time.setter
    def from_time(self, new_from_time):
        self._from_time = new_from_time

    def calculate_time(self):
        return self._to_time - self._from_time

    def __str__(self):
        return 'Scheduled from:' + str(self.from_time) + ' to ' + str(self.to_time)


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
    _dev_timer = models.OneToOneField(Timer, verbose_name='Device timer', null=True, on_delete=models.CASCADE)
    _dev_room = models.ForeignKey(Room, verbose_name='Device room', null=True, on_delete=models.CASCADE)
    _dev_name = models.CharField(verbose_name='Name of device', max_length=256)
    _modified = models.DateTimeField(verbose_name='Time modified')
    _dev_power = models.BooleanField(verbose_name='Device power')

    @property
    def timer(self):
        return self._dev_timer

    @timer.setter
    def timer(self, new_timer):
        self._dev_timer = new_timer

    @property
    def room(self):
        return self._dev_room

    @room.setter
    def room(self, new_room):
        self._dev_room = new_room

    @property
    def name(self):
        return self._dev_name

    @name.setter
    def name(self, new_name):
        self._dev_name = new_name

    @property
    def modification_time(self):
        return self._modified

    @modification_time.setter
    def modification_time(self, value):
        self._modified = value

    @property
    def power(self):
        return self._dev_power

    @power.setter
    def power(self, new_power):
        self._dev_power = new_power

    def __str__(self):
        return self._dev_name + ' in the ' + self._dev_room.name


class Sensor(models.Model):
    _critical_temperature = models.FloatField(verbose_name='Critical temperature', default=0)
    _room = models.ForeignKey(Room, verbose_name='Sensor timer', on_delete=models.CASCADE)
    _temperature = models.FloatField(verbose_name='Sensor temperature', default=0)
    _humidity = models.FloatField(verbose_name='Sensor humidity', default=0)
    _name = models.CharField(verbose_name='Sensor name', max_length=256)

    @property
    def critical_temp(self):
        return self._critical_temperature

    @critical_temp.setter
    def critical_temp(self, value):
        self._critical_temperature = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, new_humidity):
        self._humidity = new_humidity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def room(self):
        return self._room.name

    @room.setter
    def room(self, new_room):
        self._room = new_room

    def temperature_safe(self):
        if self._critical_temperature > self._temperature:
            return True
        else:
            return False

    def __str__(self):
        return self._name + ' in ' + self._room.name + ' has value' + str(self._temperature)


# TODO test profile !!!


class Profile(models.Model):
    _user = models.OneToOneField(User, on_delete=models.CASCADE)
    _device = models.ManyToManyField(Device)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, new_user):
        self._user = new_user

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, new_dev):
        self._device = new_dev

    def __str__(self):
        return ' '.join((self._user.username, self._user.first_name, self._user.last_name))
