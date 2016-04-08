#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Friends.py
@date: 16/4/8 下午5:35
"""

from RequestHandler import RequestHandler
from tornado import gen

class Friends(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        print 1