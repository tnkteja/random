from __future__ import division
import math

arthmeticsum = lambda x:  x*(x+1)/2
sumofSquaresoffirstNnaturalnumbers = lambda x:  n*(n+1)((2*n)+1)/6
geometricsum = lambda x,y:  (x**(y+1) - 1)/(x-1) if x is not 1 else y+1

sigmaieq1tokiapowi = lambda x,y:  (x - ((y+1)*x**(y+1)) + (y*(x**(y+2))))/(1-x)**2 
sigmaieqjtok1byiub = lambda x,y: math.loge(y/x-1)
stirlingsformula = lambda x:  ((2*math.pi*x)**0.5)*(x/math.e)**x
