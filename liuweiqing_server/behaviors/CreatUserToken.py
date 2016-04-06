#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: CreatUserToken.py
@date: 16/4/6 下午1:35
"""

from Behaviors import Bahaviors
from tornado import gen

class CreatUserToken(Bahaviors):

    @gen.coroutine
    def Action(self, uid, server_token, rongyun_token):
        tid = yield self.token_model.CreatToken(uid, server_token, rongyun_token)
        raise gen.Return(tid)