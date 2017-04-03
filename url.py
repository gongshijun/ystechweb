#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""


from handlers.index import IndexHandler
from handlers.matlab import MMEHandler
from handlers.dashboard import DashHandler
from handlers.login import *

url = [
    (r'/', IndexHandler),
    (r'/matlab', MMEHandler),
    (r'/dashboard', DashHandler),
    (r'/login', LoginHandler),
    ]
