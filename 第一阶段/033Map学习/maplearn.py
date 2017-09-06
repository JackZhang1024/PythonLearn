#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: mapLearn.py
@time: 2017/9/21 22:13
"""

items = [1, 2, 3, 4, 5]
results = list(map(lambda x: x**2, items))
print results


def add(x):
    return x+x


def multiply(x):
    return x*x

funcs = [add, multiply]

for i in range(1, 4):
    value = map(lambda x: x(i), funcs)
    print value

number_list = range(-4, 10)
results = list(filter(lambda x: x > 0, number_list))
print results
