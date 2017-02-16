#!/usr/bin/env python
# coding=utf-8

import tornado.options

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
define("mongodb_host", default="127.1.0.1", help="database host", type=str)
define("mongodb_username", default="", help="database user name", type=str)
define("mongodb_port", default="27017", help="database port", type=int)
define("mongodb_pwd", default="", help="database password", type=str)
define("mongodb_useDB", default="", help="using database name", type=str)

tornado.options.parse_config_file("./server.conf", final=False)
#tornado.options.parse_command_line()
