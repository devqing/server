#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: dbs.py
@date: 16/3/29 下午2:48
"""

import motor
import urls

mongo_client = motor.MotorClient('mongodb://120.25.194.185:27017')

MONGO_DATABASE = 'shark-debug'
