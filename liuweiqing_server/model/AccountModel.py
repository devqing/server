#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: AccountModel.py
@date: 16/3/29 下午1:58
"""

from Model import Model
from tornado import gen

class AccountModel(Model):

    cls = 'account'
    @gen.coroutine
    def CreatAccountIfNotExist(self, username, password, app_name, app_version):

        uid = yield self.Find(data={})