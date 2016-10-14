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
        self.expectedSequence=None
    
    def send(self):
        packet=self.sendBuffer.pop()
        def sendPacket():
            self.socket.send(packet)
        self.timer=threading.Timer(0.5,sendPacket)
        
    def receive(self):
        if packet.type = Packet.ACK:
            self.receiveCount+=1
            _,timer=self.pendingSequence=[packet.sequence]
            self.timer.cancel()
            self.send()
        if packet.sequence is self.expectedSequence:
            self.receiveBuffer.append(packet)
        #elif packet.type == Packet.NACK:
        #    packet,timer=self.pendingSequence=[packet.sequence]
        #    timer.cancel()
        #    self.socket.send(packet)
        #    timer.start()
            
            
    def sendAck(self):
        self.socket.send(PacketAck().serialize())
        
        
        
        
        
 class channel(object):
    
    def __init__(self):
        """
        Number of bits in transit on the chanel.
        """
        self.bandwidthDelayProduct= self.bandwidth * self.propagationDelay
        
        self.utilization = self.s/2*self.bandwidthDelayProduct
        
        
class SlidingWindow(object):
    
    def __init__(self):
        self.senderWindow=[0,10]
        self.receiverWindow=[0,10]