#!/usr/bin/python
import socket


# To sniff on the schared channel using Raw Socket : The network interface card should be put in Promiscious mode so that it listens on all the packets
# and provides them to the raw sockets in the broadcast medium.
# Promiscious mode - See all Listen all - Wizard mode.


# Open Raw Socket at Layer 2
s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0003))


print s.recvfrom(655)
