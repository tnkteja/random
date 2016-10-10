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
