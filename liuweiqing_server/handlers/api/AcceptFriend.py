#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: AcceptFriend.py
@date: 16/4/8 下午5:37
"""

from RequestHandler import RequestHandler
from tornado import gen

class AcceptFriend(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        print 1