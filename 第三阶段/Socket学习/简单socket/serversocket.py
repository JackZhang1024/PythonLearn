#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: serversocket.py
@time: 2017/9/12 16:50
"""


from socket import *
from time import ctime

HOST = 'localhost'
PORT = 8001
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)


def start_server():
    serv_socket = socket(AF_INET, SOCK_STREAM)
    serv_socket.bind(ADDRESS)
    serv_socket.listen(5)
    try:
        while True:
            print 'waiting for connection ...'
            tcpclisock, address = serv_socket.accept()
            print 'connection address from :', address
            while True:
                data = tcpclisock.recv(BUFFER_SIZE)
                if not data:
                    break
                tcpclisock.send('[%s] %s' % (ctime(), data))
                print [ctime()], ':', data
            tcpclisock.close()
    except socket.timeout as e:
        print 'Time is out', e
    serv_socket.close()


if __name__ == '__main__':
    start_server()
