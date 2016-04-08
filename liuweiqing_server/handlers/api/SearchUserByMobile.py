#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: SearchUserByMobile.py
@date: 16/4/8 下午5:31
"""

from RequestHandler import RequestHandler
from tornado import gen

class SearchUserByMobile(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        mobile = self.get_argument('mobile')
        print 1