#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""


from handlers.index import IndexHandler
from handlers.matlab import MMEHandler

url = [
    (r'/', IndexHandler),
    (r'/matlab', MMEHandler),
]
