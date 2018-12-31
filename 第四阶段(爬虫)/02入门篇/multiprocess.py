#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: 多进程.py
@time: 2018/6/10 21:07
@description:
"""

import os
from multiprocessing import Process


def run_proc(name):
    print 'Child process %s (%s) Running ...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s ' % (os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print 'Process will start '
        # start() 方法 用于启动进程
        p.start()
    # join()方法 用于进程间同步
    p.join()
    print 'Process end. '

