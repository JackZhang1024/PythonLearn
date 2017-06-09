#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: thread_synchro.py
@time: 2017/6/1 13:38
"""
import threading
import time


class MyThread(threading.Thread):

    def __init__(self, thread_id, thread_name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        # 获取锁
        lock.acquire()
        print_time(self.thread_name, self.counter, 2)
        # 释放锁
        lock.release()


def print_time(thread_name, counter, delay):
    while counter:
        print('currentThreadName '+thread_name+" time "+time.ctime(time.time()))
        time.sleep(delay)
        counter -= 1

lock = threading.RLock()


if __name__ == '__main__':

    threads = []

    thread = MyThread(1, 'Thread1', 3)
    thread2 = MyThread(2, 'Thread2', 3)

    thread.start()
    thread2.start()

    threads.append(thread)
    threads.append(thread2)

    # 等待所有线程的结束
    for thread in threads:
        thread.join()
    print('\nMainThread Exit')
