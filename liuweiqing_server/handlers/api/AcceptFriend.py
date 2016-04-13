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
app_key = "8brlm7ufrnrx3"
app_secret = "ssZ9TDw2v7"

os.environ.setdefault('rongcloud_app_key', app_key)
os.environ.setdefault('rongcloud_app_secret', app_secret)

rongyun_client = ApiClient()

class AcceptFriend(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        from_id=self.get_argument('from_id')
        to_id=self.get_argument('to_id')

        result = rongyun_client.message_system_publish(
            from_user_id=from_id,
            to_user_id=to_id,
            object_name='RC:InfoNtf',
            content={"message":"您已经添加他为好友,可以聊天了","extra":""}
        )

        self.render({})