#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: fabcon.py
@time: 2017/9/21 8:22
"""


def fun(n):
    a = b = 1
    for i in range(1, n):
        yield a
        a, b = b, a+b

for index in fun(4):
    print index
