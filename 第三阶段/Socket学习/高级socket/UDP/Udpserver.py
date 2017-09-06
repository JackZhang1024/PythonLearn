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


class MyUdpHander(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{0} wrote {1} ".format(self.client_address[0], data)
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    HOST, ADDRESS = 'localhost', 20001
    serverSocket = SocketServer.UDPServer((HOST, ADDRESS), MyUdpHander)
    print 'Waiting For connection...'
    serverSocket.serve_forever()
