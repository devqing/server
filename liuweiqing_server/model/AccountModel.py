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

    cls = 'account1'
    @gen.coroutine
    def CreatAccountIfNotExist(self, username, password):

        uid = self.Insert({'111':'2222'})
        # client = pymongo.MongoClient("120.25.194.185", 27017)
        # db = 'shark-debug'
        # uid =  client['shark-debug0']['account0'].insert({'111':'2222'})
        print uid