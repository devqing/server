#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Friends.py
@date: 16/4/8 下午5:35
"""

from RequestHandler import RequestHandler
from tornado import gen
from bson.objectid import ObjectId

class Friends(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        uid=ObjectId(self.get_argument('uid'))
        user = yield self.user_model.GetUserFromUid(uid)
        users = yield self.user_model.GetUsersFromIds(user['friends'])
        data=[]
        for i in users:
            friend={
                '_id':str(i['_id']),
                'nike_name':i['nike_name'],
                'avatar':i['avatar']
            }
            data.append(friend)
        result={
            'friends':data
        }
        self.render(result)