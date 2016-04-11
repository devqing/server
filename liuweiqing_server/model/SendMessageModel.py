#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: DeviceModel.py
@date: 16/3/29 下午4:53
"""

import time
from ModelTest import ModelTest

class SendMessageModel(ModelTest):
    def CreatMessage(self, from_id, to_id, message, type):#0:申请  1:同意  2:拒绝  3:其他正常消息
        condition={}
        if type==0:
            condition={
                'from_id':from_id,
                'to_id':to_id,
                'message':message,
                'type':type,
                'creat_time':int(time.time() * 1000)

            }
            uid=self.Insert(condition)
        elif type==1:
            uid=self.Update(condition)
            print 1
        elif type==2:
            print 1
        elif type==3:
            condition={
                'from_id':from_id,
                'to_id':to_id,
                'message':message,
                'type':type,
                'creat_time':int(time.time() * 1000)

            }
            uid=self.Insert(condition)
        print 1