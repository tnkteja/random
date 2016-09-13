#!/usr/bin/python
import random

def randomBirthday():
	month=random.randint(1,12)
	upbound = 30
	if month in [1,3,5,7,8,10,12]:
		upbound = 31
	elif month == 2:
		upbound = 28
	day = random.randint(1,upbound)
	upboundyear = int(time.asctime()[-4:])
	year = random.randint(upboundyear-50,upboundyear-25)
	return day,month,year

print randomBirthday()

f=open("indianfirstnames-male.txt",r")
firstnamesmale=f.read().split('\n')
f.close()

f=open("indianlastnames.txt","r")
lastnames=f.read().split('\n')
f.close()

FirtName = firstnamesmale[random.randint(0,len(firstnamesmale)-1)]
LastName = lastnames[random.randint(0,len(lastnames)-1]

print Firstname,LastName




