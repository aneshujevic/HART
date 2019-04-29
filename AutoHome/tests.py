# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from .models import *


class TimerModelTest(TestCase):
    timer = Timer(from_time=timezone.now(), to_time=timezone.now() + timedelta(1))

    def test_timer_calculate_time(self):
        print(self.timer.calculate_time())

    def test_timer_set_time(self):
        self.timer.to_time = timezone.now() + timedelta(1)
        self.timer.from_time = timezone.now()

    def test_timer_get_time(self):
        print(self.timer)
        self.test_timer_set_time()
        print(str(self.timer) + ' - modified')

    def test_zoutro(self):
        print('=== TESTING TIMER MODEL ENDED ===\n')


class RoomModelTest(TestCase):
    room = Room(name='Podrum')

    def test_aintro(self):
        print('=== TESTING ROOM MODEL STARTED ===')

    def test_room_name(self):
        value = 'Kuhinja'
        print(self.room.name)
        self.room.name = value
        print(self.room.name + ' - modified')

    def test_zoutro(self):
        print('=== TESTING ROOM MODEL ENDED ===\n')


class DeviceModelTest(TestCase):
    timer = Timer(from_time=timezone.now(), to_time=timezone.now() + timedelta(1))
    modified = timezone.now() + timedelta(1)
    room = Room(name='Kitchen')
    name = 'test_device'
    power = True
    device = Device(modification_time=modified, power=power, room=room, timer=timer, name=name)

    def test_aintro(self):
        print('\n=== TESTING DEVICE MODEL STARTED ===')

    def test_device_modification_time(self):
        mod_time = timezone.now()
        print(self.device.modification_time)
        self.device.modification_time = mod_time
        print(str(self.device.modification_time) + ' - modified')

    def test_device_room(self):
        new_room = Room(name='Basement')

        print(self.device.room.name)
        self.device.room = new_room
        print(self.device.room.name + ' - modified')

    def test_device_power(self):
        new_power = False

        print(str(self.device.power))
        self.device.power = new_power
        print(str(self.device.power) + ' - modified')

    def test_device_timer(self):
        time_from = timezone.now()
        time_to = timezone.now() + timedelta(1)

        print(self.device.timer.to_time)
        self.device.timer.from_time = time_from
        self.device.timer.to_time = time_to
        print(str(self.device.timer) + ' - modified')

    def test_device_name(self):
        name = 'new_test_device'

        print(self.device.name)
        self.device.name = name
        print(self.device.name + ' - modified')

    def test_zoutro(self):
        print('=== TESTING DEVICE MODEL ENDED ===\n')


class SensorModelTest(TestCase):
    room = Room(name="Attic")
    name = "test sensor"
    temperature = 10
    crit_temp = 20
    humidity = 15
    sensor = Sensor(name=name, room=room, temperature=temperature, critical_temp=crit_temp, humidity=humidity)

    def test_aintro(self):
        print('=== TESTING SENSOR MODEL STARTED ===')

    def test_get_attributes(self):
        print(f"Alarm temperature is {self.sensor.critical_temp}, temperature is {self.sensor.temperature}",
              f"whilst the humidity is {self.sensor.humidity}")
        print(f"{self.sensor.name} is currently at the {self.sensor.room}")

        if not self.sensor.temperature_safe():
            print("dangeraux")
        else:
            print("safe")

    def test_set_attributes(self):
        self.sensor.room = Room(name="garage")
        self.sensor.name = "new test sensor"
        self.sensor.temperature = 30
        self.sensor.critical_temp = 25
        self.sensor.humidity = 50
        self.test_get_attributes()

    def test_zoutro(self):
        print('=== TESTING SENSOR MODEL ENDED ===\n')


class ProfileModelTest(TestCase):
    # user = User(username="heheyoy", password="supersecretpassword", first_name='Subject 1',
    #             last_name='Tester 1', last_login=timezone.now())
    # user.save()

    user = User.objects.get(pk=1)

    from_time = timezone.datetime(2000, 12, 1, 1, 1, 1, 1)
    to_time = timezone.datetime(3000, 12, 1, 1, 1, 1, 1)
    timer = Timer(from_time=from_time, to_time=to_time)
    timer.save()

    modification_time = timezone.now() + timedelta(1)
    name = 'test_device, profile'
    # room = Room(name='room')
    # room.save()
    room = Room.objects.get(pk=1)

    # device = Device(timer=timer, room=room, name=name, modification_time=modification_time, power=True)
    # device.save()
    device = Device.objects.get(pk=1)

    # profile.save()
    profile = Profile.objects.get(_user=user)
    profile._device.add(device)

    def test_profile_info(self):
        print(' '.join(('User info: ', self.profile.user.first_name, self.profile.user.last_name,
                        self.profile.user.username, self.profile.user.password)))

        print(' '.join(('Device info', self.device.name)))

    def test_change_user(self):
        new_user = User(username="poyy", password="notsosecretpassword")
        self.profile.user = new_user
