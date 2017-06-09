#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: thread_queue.py
@time: 2017/6/1 13:56

下面的例子展示了一个队列对一堆数据的配合处理

"""


import Queue
import threading
import time

exitFlag = 0


class MyThread(threading.Thread):

    def __init__(self, thread_id, thread_name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.q = q

    def run(self):
        print('%s start ' % (self.thread_name,))
        process_data(self.thread_name, self.q)
        print('%s exit ' % (self.thread_name,))


def process_data(name, q):
    while not exitFlag:
        lock.acquire()
        if not work_queue.empty():
            data = q.get()
            lock.release()
            print("%s processing %s" % (name, data))
        else:
            lock.release()
        time.sleep(1)

thread_name_list = ['thread_1', 'thread_2', 'thread_3']
task_data_list = ['one', 'two', 'three', 'four', 'five', 'six']
thread_list = []
thread_id = 0
lock = threading.RLock()
work_queue = Queue.Queue(10)
# 后进先出的处理策略
# work_queue = Queue.LifoQueue(10)
# 有优先级的处理策略
# work_queue = Queue.PriorityQueue(10)


if __name__ == '__main__':

    for thread_name in thread_name_list:
        thread = MyThread(thread_id, thread_name,work_queue)
        thread.start()
        thread_list.append(thread)
        thread_id += 1

    lock.acquire()
    # 给队列添加数据
    for work in task_data_list:
        work_queue.put(work)
    lock.release()

    # 等待队列清空
    while not work_queue.empty():
        pass

    exitFlag = 1

    # 等待所有线程的结束
    for thread in thread_list:
        thread.join()
    print('\nMainThread Exit')
