import random,math

  
def quicksort(a,l,r, depth=100):
	print a,l,r,a[l:r+1]
	print "-------"
	if not depth:
		return
	lena=r-l+1
	#Base case 1
	if lena <2:
		print "less than 2"
		return
	elif lena == 2:
		if a[l] > a[r]:
			a[l],a[r]=a[r],a[l]
		print "two elements swapped"
		return
	# elif lena > 3:
	# 	pivot_candidates=[ a[i] for i in random.sample(xrange(lena), 3)]
	# 	pivot=sum(pivot_candidates)-max(pivot_candidates)-min(pivot_candidates)
	# 	i=a.index(pivot)
	# 	#swap with the last element
	# 	a[i],a[r]=a[r],a[i]
	
	pivot = a[r]
	i = r

	# print i,pivot,a
	li,ri,pivot=hoare_partition(a, l, r)
	print li,ri,pivot,a
	#sort left partition
	if li > 0:
		print a[l:li], "left"
		quicksort(a, l,li-1,depth=depth-1 )

	#sort right partition
	if li < r:
		print a[li+1:r+1],"right"
		quicksort(a,li+1,r,depth=depth-1)

def quicksort_tail_recursive_optimzed(a,l,r):
	stack=[(l,r)]
	random.shuffle(a)
	while stack:
		l,r=stack.pop()
		lena=r-l+1

		#Base case 1
		if lena <2:    continue
		elif lena == 2:
			if a[l] > a[r]:
				a[l],a[r]=a[r],a[l]
			continue
		
		pivot = a[r]
		i = r

		li,ri,pivot=hoare_partition(a, l, r)
		stack+=[(l,li-1),(li+1,r)] if  li-l  > r-li else  [(li+1,r),(1,li-1)]


def lomuto_partition(a,l,r):
    i=l
    for j in xrange(l+1,r):
        if a[j] <= a[r]:
            a[i],a[j]=a[j],a[i]
            i+=1
    a[i],a[r]=a[r],a[i]
    return i

def hoare_partition(a,l,r):
	pivot=a[r]
	li=l
	ri=r-1
	while li<=ri:
		while a[li]<pivot and li <= ri:
			li+=1
		while a[ri]>=pivot and ri >= li:
			ri-=1
		if li<=ri:
			a[li],a[ri]=a[ri],a[li]
			li+=1
			ri-=1
	a[li],a[r]=a[r],a[li]
	return li,ri,pivot

# a=[0,1,2]
# print a,hoare_partition(a, 0, len(a)-1),a
# print a
# quit()

a=range(0,11)

seed=random.random()
print "seed # :",seed
random.seed(seed)
random.shuffle(a)
print a
print quicksort_tail_recursive_optimzed(a,0,len(a)-1)
print a
quit()
print a
print lomuto_partition(a,0,len(a)-1)
print
print a
print hoare_partition(a, 0, len(a)-1)
print a
