class stopandwait(object):
    def __init__():
       self.count=0
    
    def send():
       if self.lastAck:
          self.socket.send(self.buffer.pop())
          self.lastAck=False
          
    def receive(self,packet):
        if packet.type = Packet.ACK:
            self.lastAck=True
            self.send()
        
        
