from __future__ import division
import random, math



class Node(object):

	def __init__(self,previous=None,next=None,data=None):
		self.previous=previous
		self.next=next
		self.data=data


def forward_iterator(head):
	while head:
		yield head
		head=head.next


def backward_iterator(tail):
	while tail:
		yield tail
		tail=tail.previous


def print_linkedlist(head):
	while head:
		print head,"-->",
		head=head.next

l=0
u=100
N=20
d=(u-l)/N
head=Node(data=random.random()*(u-l),next=None)
tmp=head
for i in xrange(N-1):
	tmp.next=Node(data=random.random()*(u-l),next=None)
	tmp=tmp.next


print_linkedlist(head)

def bucketSort(head,l,u,N):
	# Setup an array of initially empty "buckets" to the input size.
	buckets=[ []  for i in xrange(N)]
	f=N/(u-l)
	# bounds=[(l+i*d,l+(i+1)*d) for i in xrange(N)]
	for v in forward_iterator(head):
		buckets[int(v.data*f)].append(v)

	# Sort each bucket
	for i,v in enumerate(buckets):
		buckets[i]=sorted(v, key= lambda x:  x.data)

	head = None
	i=0
	while not buckets[i]:
		i+=1
	head = buckets[i][0]
	tail = buckets[i][-1]
	# Join the buckets
	for j in xrange(i+1,N):
		if buckets[j]:
			tail.next=buckets[j][0]
			tail=buckets[j][-1]
	return head

print print_linkedlist(bucketSort(head, l, u, N))
