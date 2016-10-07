class Datacentre(object):
    def __init__(self):
        pass
        
class TopRack(object):
    def __init__(self):
        pass
        
class AggregationSwitches(object):
    def __init__(self):
        pass
        
class AccessNetwork(object):
    """
    
    """
    def __init__(self):
        self.anticipatedBandiwidthPerDevice=None #Uplink, DownlinkPair
        
class Rack(object):
    def __init__(self, ToR=(Switch(),Switch())):
        pass
        
class Port(object):
    def __init__(self):
        pass
        
class Switch(object):
    def __init__(self):
        self.ports={}
        
class SwitchPair(object):
    def __init__(self):
        self.switchPair=(Switch(),Switch())
        
class DataCenterDistributionLayer(object):
    def __init__(self):
        pass
        
class CoreSwitchPair(object):
    def __init__(self, upstreamFirewall=None):
        self.upStreamFirewall=None

class ChokePoint(object):
    def __init__(self):
        pass
        
class Firewall(ChokePoint):
    def __init__(self):
        pass
        
class InchasisFirewall(Firewall):
    def __init__(self):
        pass
        
class ExternalFirewall(Firewall):
    def __init__(self):
        pass
        
        
