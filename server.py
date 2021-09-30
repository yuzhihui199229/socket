"""
@author yuzh
@since 2021/9/30
"""
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("get connection from ", addr)
    c.send("thank you for connecting".encode())
    c.close()
