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
from bson.objectid import ObjectId
import error


class Login(RequestHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        mobile = self.get_argument('mobile')
        password = self.get_argument('password')
        condition = {
            'username':mobile,
            'password':password
        }
        account = yield self.account_model.GetUserFromUserName(mobile)
        # username = account['username']
        if not account:
            raise error.AccoountNotExists()
        self.render({'_id':'aaaaaaaa'})
