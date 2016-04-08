#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: RefuseFriend.py
@date: 16/4/8 下午5:38
"""

from RequestHandler import RequestHandler
from tornado import gen

class RefuseFriend(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        print 1