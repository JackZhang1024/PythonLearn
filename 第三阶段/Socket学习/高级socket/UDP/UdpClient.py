#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@version: ??
@author: zfz
@license: Apache Licence
@contact: zhangfengzhou@aragoncs.com
@site: http://github.com/zhangfengzhou
@software: PyCharm
@file: UdpClient.py
@time: 2017/9/12 18:44
"""
from socket import *

HOST, ADDRESS = 'localhost', 20001


def start_client():
    client_sck = socket(AF_INET, SOCK_DGRAM)
    while True:
        send_data = raw_input(">")
        client_sck.sendto(send_data, (HOST, ADDRESS))
        recv_data = client_sck.recv(1024)
        print "SendData: {0} RecvData: {1}\r\n".format(send_data, recv_data)


if __name__ == '__main__':
    start_client()
