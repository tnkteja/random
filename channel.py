from __future__ import division
import math, sympy

class Pretty(object):
  def __repr__(self):
  	d=self.__dict__
  	return self.__class__.__name__ + '('+', '.join(['%s: %s' % (k,d[k]) for k in sorted(d.keys()) if k[0] != "_"]) + ')' + "( id:" + str(id(self)) + " )"

db = lambda x:  10**(x/10)

class Channel(Pretty):
	"""docstring for Channel"""

	def __init__(self, br=None,b=None,v=None,sr=None,snr=None):
		#self.br,self.b,self,v,self.sr,self.snr = br,b,v,sr,snr
		BR, B, SNR, V =sympy.symbols('BR B SNR V')
		dic={BR:br,B:sr or b, SNR:snr, V : v or 2 if not snr else None}
		SHANONS_EQ=BR - ((B/2) * sympy.log(1+SNR,2))
		NYQUIST_EQ=BR - (2* B * sympy.log(V,2))
		sol=sympy.solve([SHANONS_EQ, NYQUIST_EQ]+[ sympy.Eq(k,v) for k,v in dic.iteritems() if v!=None])[0]
		self.br,self.b,self.v,self.sr,self.snr=sol[BR],b or sol[B],sol[V],sol[B],sol[SNR]
		self.baudrate = (self.br/math.log(self.v,2))
		self.st=1/self.baudrate
		self.h= self.b/self.baudrate


class Formatting(Pretty):

	def __init__(self,):
		pass

microns=lambda x:  x*10**(-6)

class Spectrum(Pretty):

	def __init__(self,wv=None,freq=None,b=None,bw=None):
		WV, FREQ, B, BW = sympy.symbols('WV FREQ B BW')
		dic={WV:wv, FREQ:freq, B: None if bw and not b else 0 if not bw and not b else b , BW: None if b and not bw else (0 if not b and not bw else bw if not b else None )}
		EQ=3*10**8 - WV*FREQ
		EQ1=3*10**8 - ((WV+B)*(FREQ+BW))
		sol=sympy.solve( [EQ,EQ1]+[ sympy.Eq(k,v) for k,v in dic.iteritems() if v != None] )[0]
		self.wv,self.freq,self.b,self.bw=sol[WV],sol[FREQ],abs(sol[B]),abs(sol[BW])


class Video(Pretty):

	def __init__(self,rs,bpp,fps):
		self.rs,self.bpp,self.fps = rs,bpp,fps
		self.bitrate =self.rs[0]*self.rs[1] * bpp * fps

class Antenna(Pretty):

	def __init__(self):
		pass

class Encoding(Pretty):

	def __init__(self):
		pass

class NRZEncoding(Encoding):

	def __init__(self):
		pass
		
class ManchesterEncoding(Encoding):

	def __init__(self):
		pass

class 4B5BEncoding(Encoding):
	def __init__(self):
		pass

class BipolarEncoding(Encoding):

	def __init__(self):
		pass

class EightBTenBEncoding(Encoding):

	def __init__(self):
		pass

class Multiplexing(Pretty):

	def __init__(self, channels):
		self.channels = channels

class PassBandModulation(Pretty):

	def __init__(self):
		pass

class AmplitudShiftKeying(PassBandModulation):

	def __init__(self):
		pass

class FrequencyShiftKeying(PassBandModulation):

	def __init__(self):
		pass

class PhaseShiftKeying(PassBandModulation):

	def __init__(self):
		pass

class TimeDivisionMultiplexing(Multiplexing):

	def __init__(self,slot, channels, guard):
		super(Multiplexing,self).__init__(channels)
		self.slot = slot
		self.guard = guard


class FrequencyDivisionMultiplexing(Multiplexing):

	def __init__(self,guard, channels):
		super(Multiplexing,self).__init__(channels)
		self.guardband=guard
		self.channels = channels

class CodeDivisionMultiplexing(Multiplexing):

	def __init__(self):
		pass

class OrthogonalFrequencyDivisionMultiplexing(FrequencyDivisionMultiplexing):

	def __init__(self):
		pass

class Media(object):
	"""docstring for Media"""
	def __init__(self, noise, interference, attenuation):
		pass

class UnguidedMedia(Media):

	def __init__(self):
		pass

class GuidedMedia(Media):

	def __init__(self):
		pass

class System(object):
	
	def __init__(self):
		pass
	
class Satellite(System):
	def __init__(self,height,rotationtime, latecy, coverage,):
		self.height=height
		self.timeperiod=rotationtime
		self.latency= latency
		self.coverage=coverage

class GeostationarySatellelite(Satellite):
	def __init__(self):
		super(Satellite,self).__init__(35000,days(24),millseconds(270),None)

class MeostationarySatellite(Satellite):
	"""
	Upper Vanhelen belt and Upper Vanhelen belt.  GPS.
	"""
	def __init__(self):
		super(Satellite,self).__init__(10000,None,[milliseconds(35),milliseconds(85)],millseconds(270)],None)
	
class LeostationarySatellite(Satellite):
	"""
	Lower Vanhelen belt and Upper Vanhelen belt.
	"""
	def __init__(self):
		super(Satellite,self).__init__(None,None,None,None)
		
class Iridium(LeostationarySatellite):
	def __init__(self):
		pass
	
class Hub(object):
	def __init__(self):
		pass

class ADSL(object):
	def __init__(self):
		pass
	
class PublicTelephoneNetworks(System):
	"""3 khz
	"""
	def __init__(self):
		pass
class FiberToTheHome(object):
	"""
	"""
	def __init__(self):
		pass
class Modem(object):
	def __init__(self):
		pass

class Lastmile(object):
	def __init__(self):
		pass

class Localloop(Lastmile):
	def __init__(self):
		pass

class ADSL(Localloop):
	def __init__(self):
		pass

class FibreToTheHome(Localloop):
	def __init__(self):
		pass
	
import numpy as np
import matplotlib.plotly as plt

class FourierTransform(Pretty):

	def __init__(self):
		self.freq=4800
		T=xrange(0,1000,1)
		y=[ math.sin(2 * math.pi * self.freq *t) for t in T]
		print np.fft.fft(y)

print FourierTransform()
quit()
v=Video((2560,1600), 24, 60)
c= Channel(b=4800,v=256)
print c
sp1=Spectrum(wv=microns(1.3),bw=c.b)
print sp1
quit()
print v.bitrate
sp=Spectrum(microns(1))
print sp.bandfreq
print sp.getbandwidth(microns(0.1))
