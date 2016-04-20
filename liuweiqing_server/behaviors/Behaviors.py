#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Behaviors.py
@date: 16/3/31 下午6:25
"""

from model import UserModel
from model import TokenModel
from model import ApplyModel
from model import ImageIdModel

class Bahaviors(object):
    def __init__(self):
        super(Bahaviors, self).__init__()

    @property
    def user_model(self):
        return UserModel()

    @property
    def token_model(self):
        return TokenModel()

    @property
    def apply_model(self):
        return ApplyModel()

    @property
    def user_avatar_model(self):
        return ImageIdModel()