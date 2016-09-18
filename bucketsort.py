#!/usr/bin/python
#
"""bucketSort
"""
from __future__ import division
import random, math



class Node(object):

	def __init__(self,previous=None,next=None,data=None):
		self.previous=previous
		self.next=next
		self.data=data

	def swap_with_next(self):
		next=self.next
		if not next:
			return
		next.previous,self.previous=self.previous,next
		self.next,next.next=next.next,self

	def swap_with_previous(self):
		pass

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


def insertionSort(head,key=None):
	i=head.next
	while i:
		if key(i) <= key(i.previous):
			i.swap_with_previous()

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

"""
MIT License
Copyright (c) 2016 Neela Krishna Teja Tadikonda
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
