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
        # legend = ['A','B','C']
        # axis=[1,2,3]
        # series =[{'data':[1,2,3.3],'type':'bar'},{'data':[1.343513,3.45,5.7846],'type':'bar'},{'data':[12,4,5.56],'type':'bar'}]
        data = {'legend': legend,
                'axis': axis,
                'series': series}
        # print(data)
        self.write(data)

