#!/usr/bin/env python
# coding=utf-8

import tornado.web

class MMEHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("matlab.html")

    def post(self):
        MME = self.get_argument("MME")
        file_object = open('mme.m', 'w')
        file_object.write(MME)
        file_object.close()
        self.write("sucess!")
