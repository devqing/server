#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: JsFile.py
@date: 16/3/30 上午11:00
"""

import tornado.web
from tornado import gen

class JsFile(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.render("customer.js")