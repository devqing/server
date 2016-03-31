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
import pymongo


class AccountModel(ModelTest):

    cls = 'account'
    @gen.coroutine
    def CreatAccountIfNotExist(self, username, password):
        acount = {
            'username':username,
            'password':password

        }
        uid = yield self.Insert(acount)
        print uid