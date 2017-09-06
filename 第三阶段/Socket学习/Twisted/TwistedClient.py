#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: TwistedClient.py
@time: 2017/9/13 0:00
"""

from twisted.internet import protocol, reactor
from time import ctime

HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):

    def sendData(self):
        data = raw_input('> ')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionClost = clientConnectFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory)
reactor.run()