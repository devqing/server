#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: ApplyModel.py
@date: 16/4/19 下午2:45
"""

from ModelTest import ModelTest
from tornado import gen
import error
import time

class ApplyModel(ModelTest):

    cls = "apply"
    @gen.coroutine
    def CreatApplyIfNotExists(self, from_id, to_id):
        newFlag={'new':False,'aid':None}
        condition={
            'from_id':from_id,
            'to_id':to_id
        }
        record=yield self.Find(condition)
        if not record:
            condition={
                'from_id':from_id,
                'to_id':to_id,
                'creat_time':int(time.time()*1000)
            }
            aid=yield self.Insert(condition)
            newFlag['new']=True
            newFlag['aid']=aid
            raise gen.Return(newFlag)