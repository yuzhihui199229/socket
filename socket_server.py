"""
@author yuzh
@since 2021/9/30
"""
from socketserver import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('get connect from ', addr)
        self.wfile.write("thank you for connecting")


server = TCPServer(('', 1234), Handler)
server.serve_forever()
