#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: CreatApply.py
@date: 16/4/19 下午2:54
"""

from Behaviors import Bahaviors
from tornado import gen

class CreatApply(Bahaviors):

    @gen.coroutine
    def Action(self, from_id, to_id):
        newFlag=yield self.apply_model.CreatApplyIfNotExists(from_id, to_id)
        raise gen.Return(newFlag['new'])