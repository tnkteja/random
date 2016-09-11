
import math

lastgeneratednumber=0
digits=0

def setseed(seed_):
    global lastgegneratednumber
    lastgeneratednumber=int(seed_)
    digits=len(str(seed_))

def vanneuman():
    global lastgeneratednumber,digits
    tmp=lastgeneratednumber*lastgeneratednumber
    print tmp
    lastgeneratednumber=str(tmp)
    newdigits=len(lastgeneratednumber)
    striplength=newdigits-digits
    halfstriplength=striplength/2
    leftstrip=(striplength%2)+halfstriplength
    rightstrip=halfstriplength
    if striplength==0:
        return int(lastgeneratednumber)
    else:
        print lastgeneratednumber[leftstrip:-rightstrip]
        return int(lastgeneratednumber[leftstrip:-rightstrip])

setseed(2)
print vanneuman()
setseed(1111)
print vanneuman()     
