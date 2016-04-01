#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: RequestHandler.py
@date: 16/4/1 下午4:49
"""

from error import APIError
import base
import json
from tornado.web import MissingArgumentError

class RequestHandler(base.RequestHandler):
    def render(self, data):
        retval = {
            "flag":"ok",
            "data":data
        }
        self.write(retval)

    def initialize(self):
        super(RequestHandler, self).initialize()
        #Do not cache any content
        self.set_header('Cache-Control','no-cache, no-store, must-revalidate')#HTTP/1.1
        self.set_header('Pragma','no-cache')#HTTP/1.0
        self.set_header('Expires','0')#Proxies
        self.set_header("Content-Type", "application/json") # Set response content type

    def _handle_request_exception(self, error):
        if self._finished:
            return
        if isinstance(error, APIError):
            self.render_error(error)
        elif isinstance(error, MissingArgumentError):
            print 3
            # self.render_error(ParamInvalidError(error.arg_name))
        else:
            super(RequestHandler, self)._handle_request_exception(error)

    def write_error(self, status_code, **kwargs):
        if status_code >= 500:
            # self.render_error(UnknownError())
            print 1
        else:
            super(RequestHandler, self).write_error(status_code, **kwargs)

    def render_error(self, error):
        if self._finished:
            return
        if isinstance(error, APIError):
            result = {'flag': 'error', 'code': error.code, 'reason':error.reason}
        self.write(json.dumps(result))
        self.finish()