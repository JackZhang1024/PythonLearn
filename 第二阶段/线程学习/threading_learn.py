#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: threading_learn.py
@time: 2017/6/1 12:49
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
        print('thread start '+self.thread_name+" \n")
        print_time(self.thread_name, self.counter, 5)
        print('thread exit  '+self.thread_name+" \n")


def print_time(thread_name, counter, delay):
    while counter:
        print('currentThreadName '+thread_name+" counter "+str(counter)+"\n")
        time.sleep(delay)
        counter -= 1


if __name__ == '__main__':
    thread = MyThread(1, 'Thread1', 2)
    thread2 = MyThread(2, 'Thread2', 3)

    thread.start()
    thread2.start()

    print('\nMainThread Start')

