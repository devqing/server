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
import base
from behaviors import CreatNewUser


app_key = "8brlm7ufrnrx3"
app_secret = "ssZ9TDw2v7"

os.environ.setdefault('rongcloud_app_key', app_key)
os.environ.setdefault('rongcloud_app_secret', app_secret)

rongyun_client = ApiClient()

class SignUp(base.RequestHandler):

	@gen.coroutine
	def post(self, *args, **kwargs):
		mobile = self.get_argument('mobile')
		password = self.get_argument('password')
		uid = yield CreatNewUser().Action(mobile, password)

		result = rongyun_client.user_get_token(
            'test-userid1',
            'test-name1',
            'http://www.rongcloud.cn/images/logo.png')
		print result



