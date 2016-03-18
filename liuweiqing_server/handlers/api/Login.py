#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Login.py
@date: 16/3/15 下午4:58
"""

from tornado import gen
from bson.objectid import ObjectId
import base


class Login(base.ApiRequestHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        orderId = self.get_argument('oid')

        if orderId == 'orderId':
            print('输出正确')
        else:
            print('输出错误')
        data = {
            '_id': '123',
            'name': 'zdx',
            'age': 27

        }
        var = []
        data = {"area": var}
        self.write(data)
