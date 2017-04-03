# coding: utf-8
import os
import re
import pandas as pd

# run shell
def execmd(cmd):
    os.system(cmd)

class final_result(object):

    def __init__(self, result=None):
        self.result = result
    
    # get data from result.txt
    def get_result(self,filename):
        f = open(filename, 'r')
        data = f.read()
        f.close()
        self.result = data
        return data

    # parse data 
    def parse_result(self):
        # drop nonesense
        #tmp =re.match('^(.*\s){13}',self.result)
        tmp = re.sub('(.*\s){13}',"",self.result)
        #print(tmp)

def Result(outfile):
    FR=final_result()
    FR.get_result(outfile)
    #FR.parse_result()
    return FR.result

# csv to jason
def result2json(outfile):
    data=pd.read_table(outfile,sep=',')
    data=data.round(4)

    #print(data.head())
    data=data.unstack().unstack()
    
    #print(data.head())
    data=data.to_json()
    #print(data)
    return data
