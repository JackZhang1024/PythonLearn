#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: faboccia.py
@time: 2017/6/1 16:34
"""
import sys


def main(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = main(1000)
while True:
    try:
        result = next(f)
        print result
    except StopIteration as e:
        sys.exit()

