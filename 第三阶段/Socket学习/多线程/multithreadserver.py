#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: multithreadserver.py
@time: 2017/9/12 23:02
"""


from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH, ThreadingMixIn as TMI)
from time import ctime


HOST = 'localhost'
PORT = 8001
ADDR = (HOST, PORT)


class Server(TMI, TCP):
    pass


class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from: ', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = Server(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
