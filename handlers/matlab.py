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
        # mfile matfolder
        matfolder='matfile/'
        # result file 
        outfile='../common/result.txt'
        cmd='nohup matlab -nodesktop -nosplash -r '
        
        # get expression
        MME = self.get_argument("MME","")
        matfile = "mme" + str(int(time.time())) 
        file_object = open('./' + matfolder + matfile + '.m', 'w')
        file_object.write(MME)
        file_object.write("\n")
        file_object.write("exit()")
        file_object.close()
        # run shell command
        cmd = cmd + matfile + '>' + outfile 
        os.chdir("./matfile")
        CR.execmd(cmd)
        
        # get result
        data = CR.Result(outfile)
        os.chdir("../")
        
        # present excel
        data = CR.result2json('./common/FKPIDB.txt', sep=',')
        # write back data
        self.write(data)
