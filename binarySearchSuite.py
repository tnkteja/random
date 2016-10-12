#!/usr/bin/python

def binarySearchSuite(iterable,item,key=None, leftHanded=True, greedy=False, duplicates=False):
    def binarySearch(iterable,item,key=None,leftHanded=True, greedy=False):
        N=len(iterable)
        l=0
        r=N-1
        middle=lambda m: m if leftHanded else lambda m:  m+1
        while r-l >1:
            m=middle((l+r)/2)
            if key(item,iterable[m]):
                if greedy:  return m
                r=m
            else:
                l=m+1
        if key(item,iterable[l]):
            return l
        else:
            return None
    if duplicates:
        l=binarySearch(iterable, item, key, leftHanded=True)
        r=binarySearch(iterable, item, key, leftHanded=False)
        return (l,r)
    return binarySearch(iterable, item, key, leftHanded=leftHanded,greedy=greedy)
