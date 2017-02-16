#!/usr/bin/env python
# coding=utf-8

#import tornado.options

from pymongo import MongoClient
from configure import *
#from tornado.options import options, define

#define("mongodb_host", default="127.1.0.1", help="database host", type=str)
#define("mongodb_port", default=27017, help="database port", type=int)
#define("mongodb_username", default="", help="database username", type=str)
#define("mongodb_pwd", default="", help="database password", type=str)
#define("mongodb_useDB", default="yushuDB", help="using database name", type=str)

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

#tornado.options.parse_config_file("./server.conf", final=False)

if options.mongodb_username == "":
    uri = "mongodb://%s:%s/" % (
        quote_plus(options.mongodb_host),
        quote_plus(str(options.mongodb_port))
    )
else:
    uri = "mongodb://%s:%s@%s:%s/%s" % (
        quote_plus(options.mongodb_username), quote_plus(options.mongodb_pwd),
        quote_plus(options.mongodb_host), quote_plus(str(options.mongodb_port)),
        quote_plus(options.mongodb_useDB)
    )

client = MongoClient(uri)
db = client[options.mongodb_useDB]

def mongodb_close():
    client.close()
