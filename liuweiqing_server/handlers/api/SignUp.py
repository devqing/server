#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: SignUp.py
@date: 16/3/15 下午4:58
"""

import os
from tornado import gen
from rong import ApiClient
from RequestHandler import RequestHandler
from behaviors import CreatNewUser
import error


app_key = "8brlm7ufrnrx3"
app_secret = "ssZ9TDw2v7"

os.environ.setdefault('rongcloud_app_key', app_key)
os.environ.setdefault('rongcloud_app_secret', app_secret)

rongyun_client = ApiClient()

class SignUp(RequestHandler):

	@gen.coroutine
	def post(self, *args, **kwargs):
		mobile = self.get_argument('mobile')
		password = self.get_argument('password')

		flag = yield CreatNewUser().Action(mobile, password)
		print flag
		if not flag:
			raise error.AccountAlreadyExists()
		account = yield self.account_model.GetUserFromUserName(mobile)
		result = {
			'mobile':account['username'],
			'_id':str(account['_id'])
		}
		self.render(result)





