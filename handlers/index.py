#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import common.result as CR

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        data = {'legend':['邮件营销','联盟广告','视频广告','直接访问','搜索引擎'],
                'axis':['周一','周二','周三','周四','周五','周六','周日'],
                'series':[{'type':'line','data':[120,132,101,134,90,230,210]},
                    {'type':'line','data':[220,182,191,234,290,330,310]},
                    {'type':'line','data':[150,232,201,154,190,330,410]},
                    {'type':'line','data':[320,332,301,334,390,330,320]},
                    {'type':'line','data':[820,932,901,934,1290,1330,1320]}]}
        #print(data)
        self.write(data)

