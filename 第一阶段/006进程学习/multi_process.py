# -*- coding:utf-8 -*-

"""
创建多个进程

"""
from multiprocessing import Pool
import time,os,random

def run_proc(name):
    print('Child process pid %s  name: %s ' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('task %s run time %0.2f seconds' % (name,(end-start)))

if __name__=='__main__':
    print('Parent process %s ' % (os.getpid()))
    p=Pool(4)
    for i in range(5):
        p.apply_async(run_proc,args=(i,))
    print('Waiting for all child processing...')
    p.close()
    p.join()
    print('All child process finish!')