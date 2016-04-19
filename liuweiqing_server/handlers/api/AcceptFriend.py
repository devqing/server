#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: AcceptFriend.py
@date: 16/4/8 下午5:37
"""

import os
from RequestHandler import RequestHandler
from tornado import gen
from rong import ApiClient
import json
from bson.objectid import ObjectId


class AcceptFriend(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        from_id=self.get_argument('from_id')
        to_id=self.get_argument('to_id')

        result = self.application.rong_client.message_publish(
            from_user_id=from_id,
            to_user_id=to_id,
            object_name='RC:InfoNtf',
            content=json.dumps({"message":"您已经添加他为好友,可以聊天了","extra":""})
        )
        result = self.application.rong_client.message_publish(
            from_user_id=to_id,
            to_user_id=from_id,
            object_name='RC:InfoNtf',
            content=json.dumps({"message":"您已经添加他为好友,可以聊天了","extra":""})
        )

        push=yield self.user_model.UpdateFriendsByNewFriend(ObjectId(from_id), ObjectId(to_id))
        push=yield self.user_model.UpdateFriendsByNewFriend(ObjectId(to_id), ObjectId(from_id))

        self.render({})