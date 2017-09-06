# -*- coding:utf-8 -*-
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8001))
sock.listen(5)
while True:
    connection, address = sock.accept()
    try:
        buf = connection.recv(1024)
        if str(buf):
            print str(buf)
            connection.send('welcome to server')
        else:
            connection.send('please go out!')
    except socket.timeout as e:
        print('time out')
    connection.close()
