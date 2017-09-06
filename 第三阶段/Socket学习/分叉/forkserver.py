#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: forkserver.py
@time: 2017/9/12 22:55
"""

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH, ForkingMixIn as FMI)
from time import ctime


HOST = 'localhost'
PORT = 8001
ADDR = (HOST, PORT)


class Server(FMI, TCP):
    pass


class MyRequestHandler(SRH):

       def handle(self):
           print  '...connection from:', self.client_address
           self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = Server(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()