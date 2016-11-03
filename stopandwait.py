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
    """Flow control, Error control, a.k.a ARQ or PAR.
    We are putting a packet every roundtrip time. but to be accurate, it is 2 *delay +  transmission time to put my packet number, 
    atleast until sequence number. and the procesing delay at the receiver to recevice atleast until the sequence number and prepare 
    an acknowledgement.+ transmission time to put the ack on the link atleast until the sequence number and the processing delay on
    sender side to recognise and clear this packet as sent.
    Flow control is wait until the receiver can receiver can get the packet and process it very quickly
    """
    
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
        if not packet.integrity():
            self.socket.send(packet.nak())
        elif packet.type = Packet.ACK:
            self.receiveCount+=1
            _,timer=self.pendingSequence=[packet.sequence]
            self.timer.cancel()
            self.send()
        elif packet.type == Packet.NACK:
            packet,timer=self.pendingSequence=[packet.sequence]
            timer.cancel()
            self.socket.send(packet)
            timer.start()
        if packet.sequence is self.expectedSequence:
            self.receiveBuffer.append(packet)
        self.socket.send(packet.ack())
        #elif packet.type == Packet.NACK:

            
            
    def sendAck(self):
        self.socket.send(PacketAck().serialize())
        
        
        
"""
"""
        
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
