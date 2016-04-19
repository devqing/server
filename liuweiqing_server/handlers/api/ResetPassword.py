#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: ResetPassword.py
@date: 16/4/19 下午4:19
"""

from RequestHandler import RequestHandler
from tornado import gen
from bson.objectid import ObjectId
import error

class ResetPassword(RequestHandler):

    @gen.coroutine
    def put(self, *args, **kwargs):
        uid=ObjectId(self.get_argument('uid'))
        old_pwd=self.get_argument('old_passowrd')
        new_pwd=self.get_argument('new_password')
        user=yield self.user_model.GetUserFromUid(uid)
        if not user:
            raise error.AccoountNotExists()
        else:
            if user['password']==old_pwd:
                condition={
                   'password':new_pwd
                }
                yield self.user_model.UpdateUserInfo(uid,condition)
            else:
                error.OriginalPwdError()

        self.render({})