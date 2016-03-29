#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Model.py
@date: 16/3/29 下午1:58
"""

from base import dbs

class Model(object):

    client = dbs.mongo_client
    db = dbs.MONGODB_DATABASE
    cls = None #子类提供

    def Insert(self, *args, **kwargs):
        return self.Get_db().insert(*args, **kwargs)

    def Update(self, *args, **kwargs):
        return self.Get_db().insert(*args, **kwargs)

    def Remove(self):
        print 1

    def Find(self, *args, **kwargs):
        return self.Get_db().insert(*args, **kwargs)

    def Get_db(self):
        print self.client[self.db][self.cls]