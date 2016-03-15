#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: SignUp.py
@date: 16/3/15 下午4:58
"""

import os.path

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import pymongo
from pymongo import MongoClient

class Login(tornado.web.RequestHandler):
	def get(self):
		coll = self.application.db.blog
		blog = coll.find_one()
		if blog:
			self.render("blog.html",
				page_title = blog['title'],
				blog = blog,
				)
		else:
			self.redirect('/')