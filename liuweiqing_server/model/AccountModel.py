#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: AccountModel.py
@date: 16/3/29 下午1:58
"""
from ModelTest import ModelTest
from tornado import gen

class AccountModel(ModelTest):
    cls = 'account'
    @gen.coroutine
    def CreatAccountIfNotExist(self, username, password):

        retval = {'new':False,'uid':None}
        condition = {'username':username}
        result = yield self.Find(condition)
        if not result:
            acount = {
               'username':username,
               'password':password
            }
            uid = yield self.Insert(acount)
            retval = {'new':True,'uid':uid}
        raise gen.Return(retval)

    @gen.coroutine
    def GetUserFromUserName(self, username):
        account = {
            'username':username
        }
        result = yield self.Find(account)

        raise gen.Return(result)