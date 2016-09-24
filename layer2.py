#!/usr/bin/python
import socket

# Open Raw Socket at Layer 2
s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0003))

print s.recvfrom(655)
