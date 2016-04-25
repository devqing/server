#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Nginx.py
@date: 16/4/21 下午7:11
"""
import random
from RequestHandler import RequestHandler
from tornado import gen

class Nginx(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render({})