#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: SignUp.py
@date: 16/3/15 下午4:58
"""

from tornado import gen
import base

class SignUp(base.RequestHandler):

	@gen.coroutine
	def post(self, *args, **kwargs):
		data = {
			'_id':'123',
			'name':'zdx',
			'age':27

		}
		self.write(data)