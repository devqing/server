#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: ModelTest.py
@date: 16/3/31 下午7:44
"""

from base import dbs
import pymongo

class ModelTest(object):

    # client = pymongo.MongoClient("120.25.194.185", 27017)
    client = dbs.mongo_client
    db = 'shark-debug1'
    cls = None #子类提供
    # client = pymongo.MongoClient("120.25.194.185", 27017)
    # db = client
    def __init__(self):
        super(ModelTest, self).__init__()

    def Get_db(self):
        return self.client[self.db][self.cls]

    def Insert(self, *args, **kwargs):
        return self.Get_db().insert(*args, **kwargs)

    def Update(self, *args, **kwargs):
        return self.Get_db().insert(*args, **kwargs)

    def Remove(self):
        print 1

    def Find(self, *args, **kwargs):
        return self.Get_db().insert(*args, **kwargs)