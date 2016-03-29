#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: dbs.py
@date: 16/3/29 下午2:48
"""

import motor

mongo_client = motor.MotorClient('http')

MONGO_DATABASE = 'shark-debug'