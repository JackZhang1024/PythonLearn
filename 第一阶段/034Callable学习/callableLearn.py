#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: callableLearn.py
@time: 2017/9/23 11:39
@description: Callable可以将一个类的对象当作函数来使用 作用的结果就是在__call__方法
"""


class Speed(object):
    def __init__(self, gravity):
        self.gravity = gravity

    def __call__(self, t):
        return self.gravity*t*t*1/2

speed = Speed(9.8)
result = speed(10)
print result
