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

        user = yield self.user_model.GetUserFromMobile(mobile)
        if not user:
            raise error.AccoountNotExists()

        user = yield self.user_model.GetUserFromMobileAndPassword(mobile, password)
        if not user:
            raise error.PasswordError()

        token_result = yield self.token_model.GetTokenFromUid(str(user['_id']))
        result={
            '_id':str(user['_id']),
            'nike_name':user['nike_name'],
            'server_token':token_result['server_token'],
            'token':token_result['rongyun_token']
        }
        self.render(result)
