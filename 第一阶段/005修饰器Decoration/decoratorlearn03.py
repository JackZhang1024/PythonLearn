#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: decorationlearn003.py
@time: 2017/9/22 7:50
"""
from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper():
        print 'WrapperFunction before func'
        func()
        print 'wrapperFunction after func'
    return wrapper


@decorator
def function_a():
    print 'Hello world!!'

function_a()
print function_a.__name__

