#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: urls.py
@date: 16/3/17 下午4:06
"""

from handlers import api

urls = [
    (r"/api.login", api.Login),
    (r'/api.signup', api.SignUp),
    (r'/api.jsfile', api.JsFile),
]
