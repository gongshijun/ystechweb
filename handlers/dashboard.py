#!/usr/bin/env python
# coding=utf-8

import tornado.web
import common.result as CR

class DashHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("dashboard.html")
    
    def post(self):
        select = self.get_argument("select","")     
        data=CR.result2json('./common/FKPIDB.txt')
        print(select)
        self.write(data)
