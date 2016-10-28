#!/usr/bin/python

def binarySearchSuite(iterable,item,left=lambda x,y:  x<=y, right=lambda x,y:  x>=y,equal=None, leftHanded=True, greedy=False, duplicates=False):
    def binarySearch(iterable,item,left=lambda x,y:  x<=y, right=lambda x,y:  x>=y,equal=None,leftHanded=True, greedy=False):
        l,r=0,len(iterable)-1
        middle=lambda m: m if leftHanded else lambda m:  m+1
        while r-l >1:
            m=middle((l+r)/2)
            if left(item,iterable[m]):
                if greedy:  return m
                r=m
            else:
                l=m+1
        if equal(item,iterable[l]):
            return l
        else:
            return None
    if duplicates:
        l=binarySearch(iterable, item,left=left, right=right, equal=equal, leftHanded=True)
        r=binarySearch(iterable, item,left=left, right=right, equal=equal, leftHanded=False)
        return (l,r)
    return binarySearch(iterable, item,left=left, right=right, equal=equal, leftHanded=leftHanded,greedy=greedy)
