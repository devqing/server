#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Behaviors.py
@date: 16/3/31 下午6:25
"""

from model import AccountModel

# account_model = AccountModel()

class Bahaviors(object):
    def __init__(self):
        super(Bahaviors, self).__init__()

    @property
    def account_model(self):
        return AccountModel()