#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: DeviceModel.py
@date: 16/3/29 下午4:53
"""

from ModelTest import ModelTest
from tornado import gen

class ImageIdModel(ModelTest):

    cls = 'user_avatar'
    @gen.coroutine
    def CreatUserAvatar(self):
        condition={
            'image':'jpeg'
        }
        aid=yield self.Insert(condition)
        print aid
        raise gen.Return(aid)