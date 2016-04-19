#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: error.py
@date: 16/4/1 下午3:04
"""

class APIError(Exception):
    def __init__(self, code, reason):
        super(APIError, self).__init__()
        self.code = code
        self.reason = reason

class AccountAlreadyExists(APIError):
    def __init__(self, code=1001, reason='账户已存在'):
        super(AccountAlreadyExists, self).__init__(code, reason)

class PasswordError(APIError):
    def __init__(self, code=1002, reason='密码错误'):
        super(PasswordError, self).__init__(code, reason)

class AccoountNotExists(APIError):
    def __init__(self, code=1003, reason='账户不存在'):
        super(AccoountNotExists, self).__init__(code, reason)

class ApplyAlreadyExists(APIError):
    def __init__(self, code=1004, reason='已经发送过好友请求'):
        super(ApplyAlreadyExists, self).__init__(code, reason)

class UnknowError(APIError):
    def __init__(self, code=1005, reason='未知错误'):
        super(UnknowError, self).__init__(code, reason)

class OriginalPwdError(APIError):
    def __init__(self, code=1006, reason='旧密码错误'):
        super(OriginalPwdError, self).__init__(code, reason)