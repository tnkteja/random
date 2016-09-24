import socket

s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
s.bind((interface, 0))

# There goes plain hello world on wire 
s.send("Hello World")
