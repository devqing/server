#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: Application.py
@date: 16/4/19 下午1:36
"""

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import settings
from rong import ApiClient
import os


os.environ.setdefault('rongcloud_app_key', settings.Rong.APP_KEY)
os.environ.setdefault('rongcloud_app_secret', settings.Rong.APP_SECRET)

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self.rong_client = ApiClient()