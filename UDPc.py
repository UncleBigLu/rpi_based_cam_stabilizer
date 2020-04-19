#!/usr/bin/env python3

import socket

sAddr = '127.0.0.1'
sPort = 9999

#main
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
i = input('please input your value or press \'q\' to exit')
while(i != 'q'):
    s.sendto(i.encode('ascii'),(sAddr, sPort))
    print(s.recv(1024).decode('utf-8'))
    i = input()
# for data in [b'd1', b'd2', b'd233']:
#     s.sendto(data, (sAddr, sPort))
#     print(s.recv(1024).decode('utf-8'))
s.close()
