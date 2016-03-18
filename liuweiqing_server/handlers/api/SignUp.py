#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: SignUp.py
@date: 16/3/15 下午4:58
"""

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen

class SignUp(tornado.web.RequestHandler):

	@gen.coroutine
	def post(self, *args, **kwargs):
		data = {
			'_id':'123',
			'name':'zdx',
			'age':27

		}
		self.write(data)