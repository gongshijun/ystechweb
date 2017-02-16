#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_obj = mrd.find_from_collection(table="user", object_num=1, condition="name", value=username)
        if user_obj:
            db_pwd = user_obj['pwd']
            if db_pwd == password:
                self.write("welcome you:"+username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no this user"+username)
        # self.write(username)