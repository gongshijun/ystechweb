#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""


from handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
]
