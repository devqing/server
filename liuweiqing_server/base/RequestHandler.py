#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: RequestHandler.py
@date: 16/3/17 下午6:20
"""

import tornado.web
from model import AccountModel
from model import UserModel
from model import TokenModel

class RequestHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(RequestHandler, self).__init__(*args, **kwargs)

    @property
    def account_model(self):
        return AccountModel()

    @property
    def user_model(self):
        return UserModel()

    @property
    def token_model(self):
        return TokenModel()
