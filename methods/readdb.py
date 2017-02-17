#!/usr/bin/env python
# coding=utf-8

from methods.db import db

def find_from_collection(table, object_num, condition, value):
    col = db[table]
    if object_num == 1:
        obj = col.find_one({condition:value})
    else:
        obj = col.find({condition:value}).limit(object_num)
    return obj
