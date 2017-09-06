#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: TwistedServer.py
@time: 2017/9/12 23:35
"""
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connection from :', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection ...'
reactor.listenTCP(PORT, factory)
reactor.run()
