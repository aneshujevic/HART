# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from .models import *


# FIXME connect to models classes, this is wrong

class TimerModelTest(TestCase):
    timer = Timer(from_time=timezone.now(), to_time=timezone.now() + timedelta(1))

    def test_aintro(self):
        print('=== TESTING TIMER MODEL STARTED ===')

    def test_timer_calculate_time(self):
        print(self.timer.calculate_time())

    def test_timer_set_time(self):
        self.timer.set_time(timezone.now(), timezone.now() + timedelta(1))

    def test_timer_get_time(self):
        print(self.timer.get_time())
        self.test_timer_set_time()
        print(self.timer.get_time() + ' - modified')

    def test_zoutro(self):
        print('=== TESTING TIMER MODEL ENDED ===\n')


class RoomModelTest(TestCase):
    name = 'Podrum'
    room = Room(name)

    def test_aintro(self):
        print('=== TESTING ROOM MODEL STARTED ===')

    def test_room_name(self):
        value = 'Kuhinja'
        print(self.name)
        self.name = value
        print(self.name + ' - modified')

    def test_zoutro(self):
        print('=== TESTING ROOM MODEL ENDED ===\n')


class DeviceModelTest(TestCase):
    timer = Timer(from_time=timezone.now(), to_time=timezone.now() + timedelta(1))
    room = Room('Kitchen')
    power = True
    modified = timezone.now() + timedelta(1)
    name = 'test_device'
    device = Device(modified=modified, dev_power=power, dev_room=room, dev_timer=timer, dev_name=name)

    def test_aintro(self):
        print('\n=== TESTING DEVICE MODEL STARTED ===')

    def test_device_modification_time(self):
        mod_time = timezone.now()
        print(self.device.modification_time)
        self.device.modification_time = mod_time
        print(str(self.device.modification_time) + ' - modified')

    def test_device_room(self):
        new_room = 'Basement'

        print(self.device.room)
        self.device.room = new_room
        print(self.device.room + ' - modified')

    def test_device_power(self):
        new_power = 'False'

        print(self.device.power)
        self.device.power = new_power
        print(self.device.power + ' - modified')

    def test_device_timer(self):
        time_from_to = [timezone.now(), timezone.now() + timedelta(1)]

        print(self.device.timer)
        self.device.timer = time_from_to
        print(self.device.timer + ' - modified')

    def test_device_name(self):
        name = 'new_test_device'

        print(self.device.name)
        self.device.name = name
        print(self.device.name + ' - modified')

    def test_zoutro(self):
        print('=== TESTING DEVICE MODEL ENDED ===\n')


class ProfileModelTest(TestCase):
    user = User(username="Probni",password="12345678")
    f_name = "probno_ime"
    l_name = "probno_prezime"

    def test_aintro(self):
        print('=== TESTING PROFILE MODEL STARTED ===')

    def test_f_name(self):
        print(self.f_name)

    def test_l_name(self):
        print(self.l_name)

    def test_username(self):
        print(self.user.username)

    def test_password(self):
        print(self.user.password)

    def test_zpassword(self):
        self.change_pass('000000')
        print(self.user.password)

    def test_zoutro(self):
        print('=== TESTING ROOM MODEL ENDED ===\n')
