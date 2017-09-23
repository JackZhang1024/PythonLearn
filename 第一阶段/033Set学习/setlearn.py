#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: setlearn.py
@time: 2017/9/22 6:51
"""

# set是一个不包含重复元素的list

src = ['a', 'b', 'c', 'd', 'a', 'c', 'e']
result = set([x for x in src if src.count(x) > 1])
print result

# set交集
valid = ['red', 'blue', 'green', 'yellow', 'orange']
input_values = ['blue', 'yellow', 'brown']
set_valid = set(valid)
set_input_values = set(input_values)
set_intersection = set_valid.intersection(set_input_values)
print set_intersection
# set差集
set_difference = set_valid.difference(set_input_values)
print set_difference

a_set = {'a', 'b', 'c'}
print type(a_set)
