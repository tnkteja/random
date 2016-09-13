#!/usr/bin/python
# -*- coding: utf8 -*-
"""
The MIT License (MIT)
Copyright (c) 2016 Neela Krishna Teja Tadikonda

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, subject
to the following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class Train(Object):
    
    def __init__(self,cars,engine):
        self.cars = cars
        self.engine = engine

class Seat(object):
	"""docstring for Seat"""
	def __init__(self, position, dimensions):
		super(Seat, self).__init__()
		self.position = position
		self.dimensions = dimensions
		
class Cars(object):
	"""docstring for Cars"""
	def __init__(self, seats, dimensions):
		super(Cars, self).__init__()
		self.seats = seats
		self.dimensions = dimensions
		
class Engine(object):
	"""docstring for Engine"""
	def __init__(self, power):
		super(Engine, self).__init__()
		self.power = power
		
class Rail(object):
	"""docstring for Rail"""
	def __init__(self, separation):
		super(Rail, self).__init__()
		self.separation = separation