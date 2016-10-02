import socket, crcmod

crc=crcmod.mkCrcFun(0x104c11db7,initCrc=0,xorOut=0xffffffff)
print crc(buffer("helloworld"))

s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
s.bind((interface, 0))

# There goes plain hello world on wire 
s.send("Hello World")

