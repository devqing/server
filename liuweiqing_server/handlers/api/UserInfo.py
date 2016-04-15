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
        user = yield self.user_model.GetUserFromUid(uid)

        result={
            '_id':str(user['_id']),
            'nike_name':user['nike_name'],
            'avatar':user['avatar']
        }
        # user1=ObjectId('570f5c6a6703c06043cbd677')
        # user2=ObjectId('570f5ca06703c06043cbd679')
        # user3=ObjectId('570f5cbd6703c06043cbd67b')
        # data=[user1,user2,user3]
        # users=yield self.user_model.GetUsersFromIds(data)
        #
        # uid = yield self.user_model.UpdateFriendsByNewFriend(user1,user2)
        # print uid
        # print users
        self.render(result)