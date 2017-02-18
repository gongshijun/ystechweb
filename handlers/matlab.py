#!/usr/bin/env python
# coding=utf-8

import tornado.web
import common.result as CR
import time
import os

class MMEHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("matlab.html")

    def post(self):
        matfolder='matfile/'
        outfile='../common/result.txt'
        cmd='matlab -nodesktop -nosplash -r '

        MME = self.get_argument("MME")
        matfile = "mme" + str(int(time.time())) 
        file_object = open('./' + matfolder + matfile + '.m', 'w')
        file_object.write('f=')
        file_object.write(MME)
        file_object.write("\n")
        file_object.write("save '{0}' -ascii f;\n".format(outfile))
        file_object.write("exit()")
        file_object.close()
        #执行命令
        
        os.chdir("./matfile")
        CR.execmd(cmd + matfile)
        data=CR.get_result(outfile)
        print(data)
        os.chdir("../")
        self.write(data)
