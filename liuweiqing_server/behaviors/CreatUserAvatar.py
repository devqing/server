#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: CreatUserAvatar.py
@date: 16/4/20 下午6:51
"""

from Behaviors import Bahaviors
from tornado import gen

class CreatUserAvatar(Bahaviors):

    @gen.coroutine
    def Action(self):
        aid=yield self.user_avatar_model.CreatUserAvatar()
        raise gen.Return(aid)