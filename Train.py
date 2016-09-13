#!/usr/bin/python
# -*- coding: utf8 -*-

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