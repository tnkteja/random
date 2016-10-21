#!/usr/bin/python

"""
4. (6 points) Purpose: practice designing greedy algorithms. Suppose you
have a long straight country road with houses scattered at various points far
away from each other. The residents all want cell phone service to reach their
homes and we want to accomplish this by building as few cell phone towers
as possible.

More formally, think of points x1, …, xn, representing the houses, on the real
line, and let d be the maximum distance from a cell phone tower that will still
allow reasonable reception. The goal is to find points y1,…,yk so that, for each
i, there is at least one j with | yj - xi | ≤ d.

Describe a greedy algorithm for this problem. If the points are assumed to be
sorted in increasing order your algorithm should run in time O(n). Be sure to
describe the greedy choice and how it reduces your problem to a smaller
instance. Prove that your algorithm is correct.
"""

import random

x=sorted(random.sample(xrange(1000),500))

print x



def huffmancodes(frequencyDict):
  """
  Prefix code : no code is a prefix of another code.mp3 is encoded using huffmann code.
  """
  
frequencyDict={'e':12.702,'t':9.056,'a':8.167,'o':7.507,'i':6.966,'n':6.749,'s':6.327,'h':6.094,'r':5.987,'d':4.253,'l':4.025,'c':2.782,'u':2.758,'m':2.406,'w':2.360,'f':2.228,'g':2.015,'y':1.974,'p':1.929,'b':1.492,'v':0.978,'k':0.772,'j':0.153,'x':0.150,'q':0.095,'z':0.074}
import heapq
minheap=list(frequencyDict.items())
heapq.heapify(minheap)  #O(n)
for i in xrange()
def huffmanCompressor(text):
  pass
