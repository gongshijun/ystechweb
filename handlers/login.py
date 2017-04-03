#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("username","")
        password = self.get_argument("password","")
        user_obj = mrd.find_from_collection(table="user", object_num=1, condition="user", value=username)
        # print(user_obj)
        if user_obj:
            db_pwd = user_obj['pwd']
            if db_pwd == password:
                # self.write("welcome you:"+username)
                # print("ok1")
                self.redirect('/')
            else:
                self.write("1")
                # self.render("matlab.html")
        else:
            self.write("2")
        # self.write(username)
