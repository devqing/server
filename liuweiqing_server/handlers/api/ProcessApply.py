#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Login.py
@date: 16/3/15 下午4:58
"""

from RequestHandler import RequestHandler
from tornado import gen

class ProcessApply(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        type=self.get_argument('type')#1 同意 2 不同意
        print 1