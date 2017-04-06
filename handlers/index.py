#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import common.result as CR

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        
        filename='./common/AlphaDaily.txt'
        legend, axis, series = CR.result2echarts(filename)
        data = {'legend': legend,
                'axis': axis,
                'series': series}
        self.write(data)

