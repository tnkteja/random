#!/usr/bin/python
"""
"""

from __future__ import division
import math

class Vector(list):
    def __abs__(self):
         return sum([i**2 for i in self])**0.5
    def __mul__(self,other):
         return Vector([ v*other[i] for i,v in enumerate(other)])
         
cosinemeasure = lambda x,y:  abs(x*y)/(abs(x)*abs(y))
