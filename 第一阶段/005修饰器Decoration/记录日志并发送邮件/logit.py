#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: logit.py
@time: 2017/9/23 10:07
@description: 用于纪录日子的类
"""


from time import  ctime


class Logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func, *args, **kwargs):
        out = ctime() + ": "+'function '+func.__name__+" is called"
        print out
        with open(self.logfile, 'a') as f:
            f.write(out+"\n")
        self.notify()

    def notify(self):
        print 'log it successfully ...'
