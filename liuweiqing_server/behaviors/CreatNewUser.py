#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: CreatNewUser.py
@date: 16/3/31 下午6:25
"""

from Behaviors import Bahaviors
from tornado import gen

class CreatNewUser(Bahaviors):

    @gen.coroutine
    def Action(self, mobile, password):
        result = yield self.user_model.CreatUserIfNotExist(mobile, password)
        raise gen.Return(result['new'])