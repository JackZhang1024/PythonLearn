#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: decoratorlearn004.py
@time: 2017/9/22 7:59
"""
from functools import wraps

DEBUG = False


def decorator(func):
    def wrapper_function(*args, **kwargs):
        if DEBUG:
            print 'normal functoin is in debuging...'
        else:
            func()
    return wrapper_function


@decorator
def normal_func():
    print 'normal function is running...'

normal_func()
