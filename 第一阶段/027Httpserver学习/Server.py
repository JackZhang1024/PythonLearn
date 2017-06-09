# -*- coding:utf-8 -*-
from SocketServer import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print 'address: ',addr
        self.wfile.write('Congratulation you succeed!')

server=TCPServer(('',1234),Handler)
server.serve_forever()
