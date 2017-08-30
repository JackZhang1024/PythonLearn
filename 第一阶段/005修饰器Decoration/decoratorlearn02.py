#!/usr/bin/env python2
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: decoratorLearn02.py
@time: 2017/6/12 14:17

装饰器的学习
"""
import time


# Case 1
# def deco(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     print 'ElapsedTime ', end_time-start_time
#
#
# def my_function():
#     print 'start my_function'
#     time.sleep(3)
#     print 'end my_function'
#
# deco(my_function)
# my_function()

# Case 2

# def deco(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print 'ElapsedTime ', end_time-start_time
#     return wrapper
#
#
# def my_function():
#     print 'start my_function'
#     time.sleep(3)
#     print 'end my_function'
#
# # 将deco函数的返回值复制给my_function变量
# # 然后再去调用my_function()函数
# # 从此可以看出Python中函数可以作为返回值来处理 但是需要调用才能运行
# print 'my_function name is ', my_function.__name__
# my_function = deco(my_function)
# print 'my_function name is ', my_function.__name__
# my_function()

# Case 3

# def deco(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print 'ElapsedTime ', end_time-start_time
#     return wrapper
#
#
# # 很神奇吧 语法糖@
# @deco
# def my_function():
#     print 'start my_function'
#     time.sleep(3)
#     print 'end my_function'
#
# print 'my_function name is ', my_function.__name__
# my_function()

# 被装饰的函数带参数

# def deco(func):
#     def wrapper(a, b):
#         start_time = time.time()
#         func(a, b)
#         end_time = time.time()
#         print 'ElapsedTime ', end_time-start_time
#     return wrapper
#
#
# # 很神奇吧
# @deco
# def my_function(a, b):
#     print 'start my_function'
#     time.sleep(3)
#     print 'final result ', a+b
#     print 'end my_function'
#
# print 'my_function name is ', my_function.__name__
# my_function(4, 6)


# 装饰器带参数
# def deco(debug):
#     if debug:
#         def _deco(func):
#             def wrapper(a, b):
#                 start_time = time.time()
#                 print 'startTime ', time.ctime(start_time)
#                 func(a, b)
#                 end_time = time.time()
#                 print 'endTime ', time.ctime(end_time)
#                 print 'ElapsedTime ', end_time - start_time
#             return wrapper
#     else:
#         def _deco(func):
#             return func
#     return _deco
#
#
# @deco(True)
# def my_function(a, b):
#     print 'start my_function'
#     time.sleep(3)
#     print 'final result ', a + b
#     print 'end my_function'
#
#
# print 'my_function name is ', my_function.__name__
# my_function(4, 6)

# 装饰器的调用先后顺序

# def deco0(func):
#     def wrapper(a, b):
#         print 'decor0 start'
#         func(a, b)
#         print 'decor0 end'
#     return wrapper
#
#
# def deco1(func):
#     def wrapper(a, b):
#         print 'decor1 start'
#         func(a, b)
#         print 'decor1 end'
#     return wrapper
#
#
# @deco1
# @deco0
# def my_function(a, b):
#     print 'my_function start'
#     print 'my_function result is ', a+b
#     print 'my_function end'
#
# my_function(3, 9)

class Foo(object):
    def __init__(self, var):
        super(Foo, self).__init__()
        self._var = var

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, var):
        self._var = var

foo = Foo('var 1')
print foo.var
foo.var = 'var 2'
print foo.var

