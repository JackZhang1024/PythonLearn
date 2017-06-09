#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: start_new_thread.py
@time: 2017/6/1 11:18
"""
import thread
import time


def print_text(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print "%s,%s" % (thread_name, time.ctime(time.time()))
        count += 1

if __name__ == '__main__':
    try:
        thread.start_new_thread(print_text, ('Thread_name_1', 5))
        thread.start_new_thread(print_text, ('Thread_name_2', 5))
    except RuntimeError:
        print '发生错误'