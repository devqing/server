#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: ApiRequestHandler.py
@date: 16/3/17 下午5:39
"""

from RequestHandler import RequestHandler


class ApiRequestHandler(RequestHandler):
    def render(self, data):
        retval = {
            "flag":"ok",
            "data":data
        }
        self.write(retval)

    def render_error(self, error):
        retval = {
            "flag":"error",
            "data":error
        }
        self.write(retval)
