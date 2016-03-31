#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: DeviceModel.py
@date: 16/3/29 下午4:53
"""

from tornado import gen
from ModelTest import ModelTest

class DeviceModel(ModelTest):

    cls = "device"
    @gen.coroutine
    def Action(self, os_version, screen_witdh, screen_height):
        print 1