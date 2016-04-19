#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: ApplyFriend.py
@date: 16/4/8 下午5:36
"""

from RequestHandler import RequestHandler
from tornado import gen
import json
from behaviors import CreatApply
import error

class AppleFriend(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        fromId = self.get_argument('from_id');
        toId = self.get_argument('to_id');

        flag=yield CreatApply().Action(fromId, toId)
        if not flag:
            error.ApplyAlreadyExists()
        else:
            result = self.application.rong_client.message_system_publish(
                from_user_id=100000,
                to_user_id=toId,
                object_name='RC:ContactNtf',
                content=json.dumps({"operation":"Request","sourceUserId":fromId,"targetUserId":toId,"message":"申请添加好友","extra":""}),
                push_content='添加好友',
                push_data='添加好友'
            )

        self.render({})