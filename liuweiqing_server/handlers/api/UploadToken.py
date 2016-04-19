#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: UploadToken.py
@date: 16/4/18 下午2:08
"""

import base64
from RequestHandler import RequestHandler
from tornado import gen
import time
import json
import hmac
from hashlib import sha1
import settings

class UploadToken(RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        uid=self.get_argument('uid')
        condition="{\"scope\":\"liuweiqing\",\"deadline\":%d}"%(int(time.time()))
        encoded = base64.b64encode(condition)
        has = hmac.new(settings.Qiniu.SECRET_KEY, encoded, sha1)
        encodedSign = base64.b64encode(has.digest())

        upload_token="%s:%s:%s"%(settings.Qiniu.ACCESS_KEY,encodedSign,encoded)

        self.render({"token":upload_token,'key':uid})

