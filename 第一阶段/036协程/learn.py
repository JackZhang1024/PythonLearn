#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: learn.py
@time: 2017/9/23 20:01
@description: 协程学习
"""


def grep(pattern):
    print 'pattern is ', pattern
    while True:
        line = (yield)
        if pattern in line:
            print line

search = grep('love')
next(search)

search.send('hello world')
search.send('I Love the World')
search.send('I love the World')
search.close()
