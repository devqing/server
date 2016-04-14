#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: UserModel.py
@date: 16/4/6 上午10:58
"""

import time
from ModelTest import ModelTest
from tornado import gen
from bson.objectid import ObjectId
class UserModel(ModelTest):
    cls = 'user'
    @gen.coroutine
    def CreatUserIfNotExist(self, mobile, password):
        newFlag={'new':False,'uid':None}
        condition={
            'mobile':mobile
        }
        user = yield self.Find(condition)
        friends = []
        if not user:
            condition = {
                'mobile':mobile,
                'password':password,
                'nike_name':'悟空',
                'friends':friends,
                'avatar':'http://7xpt10.com1.z0.glb.clouddn.com/default.png',
                'creat_time':int(time.time() * 1000)
            }
            uid = yield self.Insert(condition)
            newFlag={'new':True,'uid':uid}
        raise gen.Return(newFlag)

    @gen.coroutine
    def GetUserFromMobile(self, mobile):
        condition={
            'mobile':mobile
        }
        user = yield self.Find(condition)

        raise gen.Return(user)

    @gen.coroutine
    def GetUserFromMobileAndPassword(self, mobile, password):
        condition={
            'mobile':mobile,
            'password':password
        }
        user = yield self.Find(condition)
        raise gen.Return(user)

    @gen.coroutine
    def GetUserFromUid(self, uid):
        condition={
            "_id":uid
        }
        user=yield self.Find({"_id": ObjectId("570f5c6a6703c06043cbd677")})

        # raise gen.Return(user)

    @gen.coroutine
    def GetUsersFromIds(self, ids):

        condition={"_id":{"$in":ids}}
        users=yield self.Find(condition)
        raise gen.Return(users)