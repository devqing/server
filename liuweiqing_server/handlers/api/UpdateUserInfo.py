#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: UpdateUserInfo.py
@date: 16/4/18 上午11:18
"""

from RequestHandler import RequestHandler
from tornado import gen
from bson.objectid import ObjectId
import settings

class UpdateUserInfo(RequestHandler):

    @gen.coroutine
    def put(self, *args, **kwargs):
        uid=ObjectId(self.get_argument('uid'))

        avatar=self.get_argument('avatar', None)
        nike_name=self.get_argument('nike_name', None)
        unique_name=self.get_argument('unique_name', None)
        sex=self.get_argument('sex', None)
        signature=self.get_argument('signature', None)
        conditon={}

        if avatar is not None:
            conditon['avatar']="%s/%s"%(settings.Qiniu.URL,avatar)
        if nike_name is not None:
            conditon['nike_name']=nike_name
        if unique_name is not None:
            conditon['unique_name']=unique_name
        if sex is not None:
            conditon['sex']=sex
        if signature is not None:
            conditon['signature']=signature

        update_result=yield self.user_model.UpdateUserInfo(uid,conditon)
        print update_result
        user=yield self.user_model.GetUserFromUid(uid)
        token_result = yield self.token_model.GetTokenFromUid(str(user['_id']))
        result={
            '_id':str(user['_id']),
            'nike_name':user['nike_name'],
            'server_token':token_result['server_token'],
            'token':token_result['rongyun_token'],
            'avatar':user['avatar'],
            'unique_name':user['unique_name'],
			'sex':user['sex'],
			'signature':user['signature']
        }
        self.render(result)



