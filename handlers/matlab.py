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
        # m文件的目录
        matfolder='matfile/'
        # 结果重定向的位置
        outfile='../common/result.txt'
        cmd='nohup matlab -nodesktop -nosplash -r '
        
        # 获得网页上的内容
        MME = self.get_argument("MME","")
        matfile = "mme" + str(int(time.time())) 
        file_object = open('./' + matfolder + matfile + '.m', 'w')
        file_object.write(MME)
        file_object.write("\n")
        file_object.write("exit()")
        file_object.close()
        # 执行shell命令
        cmd = cmd + matfile + '>' + outfile 
        os.chdir("./matfile")
        CR.execmd(cmd)
        
        # 获取结果
        data = CR.Result(outfile)
        #print(data)
        os.chdir("../")
        
        #动态显示表格
        data = CR.result2json('./common/FKPIDB.txt')
        #显示结果到网页上
        #print(data)
        self.write(data)
        #self.render('matlab.html',data=data)
