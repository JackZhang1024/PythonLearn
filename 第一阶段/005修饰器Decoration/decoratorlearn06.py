#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: decoratorlearn006.py
@time: 2017/9/23 9:41
@descrption: 带参数的装饰器
"""


from functools import wraps
from time import ctime


def logit(logfile='out.log'):
    def decorator_logging(func):
        @wraps(func)
        def decorator_func(*args, **kwargs):
            out = "function name "+func.__name__+" is called"
            print out
            # 将日志输入到指定的log文件中
            with open(logfile, 'a') as f:
                f.write(str(ctime()) + ": " + out+"\n")
        return decorator_func
    return decorator_logging


@logit('out0.log')
def function_add(x, y):
    return x+y


@logit('out1.txt')
def function_minus(x, y):
    return x-y

result = function_add(1, 2)
result2 = function_minus(5, 1)
