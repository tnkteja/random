class stopandwait(object):
    """Don't overflow the receviver , do the ack , with the flow control. noiseless channel.
    """
    def __init__():
       self.sendCount=0
       self.receiveCount=0
    
    def send():
       if self.lastAck:
          self.socket.send(self.buffer.pop())
          self.sendCount+=1
          self.lastAck=False
          
    def receive(self,packet):
        if packet.type = Packet.ACK:
            self.lastAck=True
            self.receiveCount+=1
            self.send()
        else:
            self.buffer.append(packet)
            
    def sendAck(self):
        self.socket.send(PacketAck().serialize())
        
        
import threading,random

class stopandwaitNoisy(object):
    
    def __init__():
        self.pendingSequence=[None]*2
        self.startSequence = 0 if random.random() < 0.5 else 1
    
    def send(self):
        packet=self.buffer.pop()
        def sendPacket():
            self.socket.send(packet)
        self.timer=threading.Timer(0.5,sendPacket)
        
    def receive(self):
        if packet.type = Packet.ACK:
            self.receiveCount+=1
            _,timer=self.pendingSequence=[packet.sequence]
            self.timer.cancel()
            self.send()
        if packet
        #elif packet.type == Packet.NACK:
        #    packet,timer=self.pendingSequence=[packet.sequence]
        #    timer.cancel()
        #    self.socket.send(packet)
        #    timer.start()
            
            
    def sendAck(self):
        self.socket.send(PacketAck().serialize())
