#!/usr/bin/python

def quicksort(arr):
    """
    basic operations:
    Running time analysis: 
    Best case -
    Average C
    """
    def hoare_partition(a,l,r):
        pivot=a[r]
        li=l
        ri=r-1
        while True:
            while a[li]<pivot and li < ri:
                li+=1
            while a[ri]>=pivot and ri >= li:
                ri-=1
            if ri < li:
                break
            a[li],a[ri]=a[ri],a[li]
        return pivot

    if len(arr
           
           
     
