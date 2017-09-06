#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: tcpserver.py
@time: 2017/9/12 17:43
"""

import SocketServer


class MyTcpHander(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{0} wrote {1} ".format(self.client_address[0], self.data)
        self.request.sendall(self.data.upper())


if __name__ == '__main__':
    HOST, ADDRESS = 'localhost', 20001
    SocketServer.TCPServer.allow_reuse_address = True
    serverSocket = SocketServer.TCPServer((HOST, ADDRESS), MyTcpHander)
    print 'Waiting For connection...'
    serverSocket.serve_forever()
