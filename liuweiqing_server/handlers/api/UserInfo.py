#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: UserInfo.py
@date: 16/4/13 下午4:03
"""

from RequestHandler import RequestHandler
from tornado import gen
from bson.objectid import ObjectId

class UserInfo(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        uid=ObjectId(self.get_argument('uid'))
        user=yield self.user_model.GetUserFromUid(uid)
        result={
            '_id':str(user['_id']),
            'nike_name':user['nike_name'],
            'avatar':user['avatar']
        }
        self.render(result)