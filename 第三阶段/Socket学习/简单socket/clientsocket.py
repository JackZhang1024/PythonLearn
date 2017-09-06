#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: clientsocket.py
@time: 2017/9/12 16:51
"""

from socket import *


HOST = 'localhost'
PORT = 8001
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)


def start_client():
    tcpclisock = socket(AF_INET, SOCK_STREAM)
    tcpclisock.connect(ADDRESS)
    while True:
        data = raw_input('>')
        if not data:
            break
        tcpclisock.send(data)
        data = tcpclisock.recv(BUFFER_SIZE)
        if not data:
            break
        print data
    tcpclisock.close()


if __name__ == '__main__':
    start_client()
