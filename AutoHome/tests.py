# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta, datetime

from .models import *


class DeviceModelTest(TestCase):
    timer = Timer(from_time=timezone.now(), to_time=timezone.now() + timedelta(1))
    room = Room('Kitchen')
    power = True
    modified = timezone.now() + timedelta(1)
    device = Device(modified=modified, power=power, room=room, timer=timer, name='test_device')

    def test_device_timer_calculate_time(self):
        self.device.timer.calculate_time()
