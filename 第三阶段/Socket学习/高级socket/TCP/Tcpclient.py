#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: tcpclient.py
@time: 2017/9/12 17:43
"""

from socket import *
import time


HOST = 'localhost'
PORT = 20001
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)


def start_client():
    tcpclisock = socket(AF_INET, SOCK_STREAM)
    tcpclisock.connect(ADDRESS)
    try:
        while True:
            data = raw_input('>')
            if not data:
                break
            tcpclisock.send(data)
            time.sleep(1)
            data = tcpclisock.recv(BUFFER_SIZE)
            if not data:
                break
            print data
    except timeout as e:
        print e
    # tcpclisock.close()


if __name__ == '__main__':
    start_client()
