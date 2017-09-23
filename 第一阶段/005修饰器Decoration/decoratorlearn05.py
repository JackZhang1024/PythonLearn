#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: decorationlearn05.py
@time: 2017/9/23 9:27
"""

from functools import wraps


def logit(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print func.__name__
        print 'logging it ....'
        return func(*args, **kwargs)
    return decorator


@logit
def do_match(x):
    return x**2
result = do_match(4)
