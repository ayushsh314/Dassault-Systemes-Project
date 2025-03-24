#!/usr/bin/env python3
# -- coding: utf-8 --

import socket
import os
import capture

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=int(input('Enter port number'))
s.bind((socket.gethostbyname(''), port)) #if the clients/server are on different network you shall bind to ('', port)
print(socket.gethostbyname(''))
s.listen(10)
c, addr = s.accept()
print('{} connected.'.format(addr))
capture.capt()
print('Captured image')
f = open("178.jpg", "rb")
l = os.path.getsize("178.jpg")
m = f.read(l)
c.send(m)
f.close()
print("Done sending...")
