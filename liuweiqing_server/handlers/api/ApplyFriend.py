#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: ApplyFriend.py
@date: 16/4/8 下午5:36
"""

from RequestHandler import RequestHandler
from tornado import gen

class AppleFriend(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        fromId = self.get_argument('from_id');
        toId = self.get_argument('to_id');
        print 1