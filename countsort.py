def Countsort(arr,l,u):
    count=[0]*(u-l+1)
    for i in arr:
        count[i] =  count[i]+1 if dic.has_key(i) else 1
    j=0
    for i,v in enumerate(count):
       for k in xrange(v):
           arr[i]= k+i
           j+=1
    return arr
    
