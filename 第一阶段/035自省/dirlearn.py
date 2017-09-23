#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: dirlearn.py
@time: 2017/9/23 19:26
@description:
"""

# my_list = ['1', '2', '3']
# # print dir(my_list)
# print dir()

# 列表推导式
ranges = [i for i in range(0, 100) if i % 2 is 0]
print ranges

# 字典推导式
dicts = {'name': 'zhang', 'age': '24', 'location': 'beijing'}
my_dicts = {k.capitalize(): v.capitalize() for k, v in dicts.items()}
print my_dicts

squard = {x**2 for x in range(0, 3)}
print squard

