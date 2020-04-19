#!/usr/bin/env python3

'''this program start udp server on raspberrypi and recv command from client to control the motor'''

import socket

port = 9999

#main
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', port))
print('Bind UDP on port: ', port)

while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s' %addr)
    data = str(int(data) +1)
    s.sendto(b'value + 1 =  %s!' %data.encode('ascii'), addr)
