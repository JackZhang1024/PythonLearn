# -*- coding:utf-8 -*-
import socket
import urlparse
import sys

def httpServer(url):
    u=urlparse.urlparse(url)
    host=u[0]
    page=u[1]
    s=socket.socket()
    port=80
    s.connect((host,port))
    httpCmd='get'+page+"\n"
    s.send(httpCmd)
    print s.recv(1024)
    s.close()


if __name__=='__main__':
    #调用httpServer()方法，传递url
    httpServer('http://snaps.php.net/index.php')



