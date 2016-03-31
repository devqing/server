#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuweiqing
@software: PyCharm Community Edition
@file: app.py
@date: 16/3/16 下午6:46
"""

import os.path

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from urls import urls


define("port", default=1880, help="run on the given port", type=int)


def main():
	tornado.options.parse_command_line()
	app = tornado.web.Application(
        urls,
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
	main()