#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: TokenModel.py
@date: 16/4/6 下午1:30
"""

import time
from ModelTest import ModelTest
from tornado import gen

class TokenModel(ModelTest):
    cls = 'token'
    @gen.coroutine
    def CreatToken(self, uid, server_token, rongyun_token):
        conditon={
            'user_id':uid,
            'server_token':server_token,
            'rongyun_token':rongyun_token,
            'creat_time':int(time.time() * 1000)
        }
        tid = yield self.Insert(conditon)
        raise gen.Return(tid)

    @gen.coroutine
    def GetTokenFromTid(self, tid):
        condition={
            '_id':tid
        }
        token=yield self.Find(condition)
        raise gen.Return(token)

    @gen.coroutine
    def GetTokenFromUid(self, uid):
        condition={
            'user_id':uid
        }
        token=yield self.Find(condition)
        raise gen.Return(token)