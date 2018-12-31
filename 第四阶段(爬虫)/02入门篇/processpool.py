#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: processpoll.py
@time: 2018/6/10 21:50
@description: 进程池
"""
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print 'Task name is %s(pid = %s) is running ...' % (name, os.getpid())
    time.sleep(random.random()*3)
    print 'Task %s end' % name

if __name__ == '__main__':
    print 'current process %s' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(str(i),))
    print 'Waiting for all process ends'
    # 执行close() 方法之后就不能再加入进程
    p.close()
    # join()会一直等到所有的子进程运行结束 join()方法一般放在close()方法之后
    p.join()
    print 'All subProcess done!'
