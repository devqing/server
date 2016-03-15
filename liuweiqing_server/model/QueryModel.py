#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: QueryModel.py
@date: 16/3/15 下午6:43
"""

import pymongo
from pymongo import MongoClient

def query(username,pwd):

        client = pymongo.MongoClient("120.25.194.185", 27017)
		db = client["Test_mongo"]
		table = db["test"]
		table.insert({'name':'zdx','age':25})
		print a
		for u in table.find():
			print u