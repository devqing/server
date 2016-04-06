#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Behaviors.py
@date: 16/3/31 下午6:25
"""

from model import AccountModel
from model import UserModel
from model import TokenModel

class Bahaviors(object):
    def __init__(self):
        super(Bahaviors, self).__init__()

    @property
    def user_model(self):
        return UserModel()

    @property
    def token_model(self):
        return TokenModel()