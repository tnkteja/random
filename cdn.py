import place

class cdn(o):
  def __init__(self, location=place(),):
    pass
    
class datacenter(o):
  def __init__(self):
    """An Internet point of presence typically houses servers, routers,
       network switches, multiplexers, and other network interface equipment.
    """
    self.pop=[]
    
class isp(o):
  def __init__(self):
    """
    """
    def __init__(self):
       pass
       
class tier1isp(isp):
  pass

class  tier2isp(isp):
"""Tier 2 network: A network that peers with some networks,
but still purchases IP transit or pays settlements to reach at least some portion of the Internet.
"""
  pass

class tier3isp(isp):
"""Tier 3 network: A network that solely purchases transit fromother networks to participate in the Internet.
"""
  pass

class regionaltier1(isp):
"""
 A regional tier 1 network is a network which is not transit free globally, but which maintains many of the classic behaviors and motivations of a tier 1 network within a specific region.

A typical scenario for this characteristic involves a network that was the incumbent telecommunications company in a specific country or region, usually tied to some level of government-supported
monopoly. Within their specific countries or regions of origin, these networks maintain peering policies which mimic those of tier 1 networks (such as lack of openness to new peering relationships 
and having existing peering with every other major network in that region). However, this network may then extend to another country, region, or continent outside of its core region of operations, 
where it may purchase transit or peer openly like a tier 2 network.
"""
  pass
  
class apisp(isp):
  pass
  
class mpisp(isp):
"""
A mailbox provider is an organization that provides services for hosting electronic mail domains with access to storage for mail boxes.
It provides email servers to send, receive, accept, and store email for end users or other organizations.
"""
  pass
  
class hostingisp(isp):
"""
Internet hosting services provide email, web-hosting, or online storage services. Other services include virtual server, cloud services, or physical server operation.
"""
  pass

class tisp(isp):
  pass

class visp(isp):
  pass

class fisp(isp):
  pass
  
class wisp(isp):
  pass
