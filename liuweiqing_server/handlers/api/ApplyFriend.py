#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: ApplyFriend.py
@date: 16/4/8 下午5:36
"""

import os
from RequestHandler import RequestHandler
from tornado import gen
from rong import ApiClient
import json

app_key = "8brlm7ufrnrx3"
app_secret = "ssZ9TDw2v7"

os.environ.setdefault('rongcloud_app_key', app_key)
os.environ.setdefault('rongcloud_app_secret', app_secret)

rongyun_client = ApiClient()

class AppleFriend(RequestHandler):

    @gen.coroutine
    def post(self, *args, **kwargs):
        fromId = self.get_argument('from_id');
        toId = self.get_argument('to_id');
        result = rongyun_client.message_publish(
            from_user_id='test-userid1',
            to_user_id='test-userid2',
            object_name='RC:TxtMsg',
            content=json.dumps({"content":"hello"}),
            push_content='thisisapush',
            push_data='aa')

        print result