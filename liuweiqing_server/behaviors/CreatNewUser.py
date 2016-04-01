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
    def Action(self, username, password):
        result = yield self.account_model.CreatAccountIfNotExist(username, password)
        raise gen.Return(result['new'])