#!/usr/bin/python
# coding: utf8

__author__ = "ntadiko"

from collections import defaultdict, deque
from itertools import groupby
import heapq



class graph(object):
    """Space Complexity is v + 2 * e
    Some graph types : star graphs and fully connected graphs.

    vertices are stored as like this .. 
    {
      vertex1: [ 
                vertexi: costfunction,
                vertexj: costfunction
            ],
      vertex2: [
                ....
                ....
            ]
            ...
    }
    Initialising the graph is n time constant time complexity.
    """

    def __init__(self,vertices=[]):
        self.root=vertices[0]
        """
        Adding entries to dict is O(1) operation, so for n entries it is n time constant time.
        """
        self.vertices={}
        for vertex in vertices:
            self.vertices[vertex]={}

    def addVertex(self,vertex):
        self.vertices[vertex]={}

    def addAdjacency(self,vertex,vertices):
        for v,costfunction in vertices:
            self.vertices[vertex][v]=costfunction

    def __repr__(self):
        return '\n'.join([str(v)+" -> "+", ".join([ str(adj) for adj in self.vertices[v]]) for v in self.vertices ])

    def bfs(self,returnPath=False):
        seen={}
        for node in self.vertices:
            seen[node]=False
        q=deque()
        goal=self.vertices[vertex]
        #Initialize a stack of paths with the one-node path consisting of the initial state
        s=[start or self.vertices[0]]
        #While (stack not empty)
        while s:
            node=s.popleft() #Pop top path
            seen[node]=True
            if node is goal:
                return True
            #If last node on path matches goal, return path
            #Else extend the path by one node in all possible ways, 
            # by generating successors of the last node on the path
            else:
                for adj in node.al:
                    if not seen[adj]:
                        s.append(adj)
        return False

    def bfsp(self,vertex,start=None):
        seen={}
        for v in self.vertices:
            seen[v]=False 
        q=[] #stack
        #Initialize a stack of paths with the one-node path consisting of the initial state
        q=deque([([start or self.root],0)])
        #While (stack not empty)
        while q:
            path,pathcost=q.popleft() #Pop top path
            seen[path[-1]]=True
            if path[-1] is vertex:
                return path,pathcost
            else:
                for adj,costfunction in self.vertices[path[-1]].items():
                    if not seen[adj]:
                        newpath=path[::]
                        newpathcost= pathcost+costfunction(path[-1],adj)
                        newpath.append(adj)
                        q.append((newpath,newpathcost))
        return None

    def dfs(self, vertex, start=None):
        seen={}
        for node in self.vertices:
            seen[node]=False
        s=[] #stack
        goal=self.vertices[vertex]
        #Initialize a stack of paths with the one-node path consisting of the initial state
        s=[start or self.vertices[0]]
        #While (stack not empty)
        while s:
            node=s.pop() #Pop top path
            seen[node]=True
            if node is goal:
                return True
            #If last node on path matches goal, return path
            #Else extend the path by one node in all possible ways, 
            # by generating successors of the last node on the path
            else:
                for adj in node.al:
                    if not seen[adj]:
                        s.append(adj)
        return False


    def dfsp(self, vertex, start=None):
        seen={}
        for v in self.vertices:
            seen[v]=False 
        s=[] #stack
        #Initialize a stack of paths with the one-node path consisting of the initial state
        s=[([start or self.root],0)]
        #While (stack not empty)
        while s:
            path,pathcost=s.pop() #Pop top path
            seen[path[-1]]=True
            if path[-1] is vertex:
                return path,pathcost
            else:
                for adj,costfunction in self.vertices[path[-1]].items():
                    if not seen[adj]:
                        newpath=path[::]
                        newpath.append(adj)
                        newpathcost= pathcost+costfunction(path[-1],adj)
                        s.append((newpath, newpathcost))
        return None

        def dfst(self, start=None):
            seen={}
            for node in self.vertices:
                seen[node]=False 
            s=[] #stack
            goal=self.vertices[vertex].data
            #Initialize a stack of paths with the one-node path consisting of the initial state
            s=[[start or self.vertices[0].data]]
            #While (stack not empty)
            while s:
                path=s.pop() #Pop top path
                seen[path[-1]]=True
                if path[-1] is goal:
                    return path
                #If last node on path matches goal, return path
                #Else extend the path by one node in all possible ways, 
                # by generating successors of the last node on the path
                else:
                #Push successor paths on top of stack Return FAIL
                    for adj in self.vertices[path[-1]].al:
                        if not seen[adj]:
                            newpath=path[::]
                            s.append(newpath.append(adj.data))
            return None

    def astar(self, returnPath=False,heuristic=None):
        self.seen={}
        for node in self.vertices:
            self.seen[node]=False
        pq=[] #heapq
        pq=[start or self.vertices[0]]
        #While (stack not empty)
        while s:
            node= s.pop() #Pop top path
            seen[node]=True
            if node is goal:
                return True
            #If last node on path matches goal, return path
            #Else extend the path by one node in all possible ways, 
            # by generating successors of the last node on the path
            else:
                for adj in node.al:
                    if not seen[adj]:
                        s.append(adj)
        return False;

    def ucsp(self,vertex,start=None):
        """Uniform Cost Search can also be considered as greedy search.

        Comments: we are doing a step of removing duplicate paths, by just keeping
        path with minimum cost.
        """
        seen={}
        for v in self.vertices:
            seen[v]=False
        pq=[] #heapq
        #Initialize a priority queue of paths with the one-node path consisting of the initial state
        pq=[(0, [start or self.root])]
        #While (queue not empty)
        while pq:
            #Remove path at root (which will be of min cost)
            pathcost, path=heapq.heappop(pq)
            seen[path[-1]]=True
            #If last node on path matches goal, return path
            if path[-1] is vertex:
                return path,pathcost
            #Else extend the path by one node in all possible ways, by generating successors of the last node on the path
            else:
                #Foreach successor path succ

                for adj,costfunction in self.vertices[path[-1]].items():
                    if not seen[adj]:
                        newpath=path[::]
                        newpath.append(adj)
                        #Update path cost to succ
                        newpathcost =  pathcost + costfunction(path[-1], adj )
                        #Insert succ on queue and re-heapify
                        #using PATH COST FROM START NODE as the priority
                        heapq.heappush(pq, ( newpathcost, newpath))
                #If two or more paths reach the same node, delete all paths except
                    #the one of min cost

                pq=sorted(pq, key=lambda x:  (id(x[1][-1]), x[0]))
                newpq=[]
                for _,it in groupby(pq, key=lambda x:  id(x[1][-1])):
                    heapq.heappush(newpq, it.next())
                pq=newpq

        return None

    def dfid(self, returnPath=False):
        """Depth First Iterative Deepining
        """
        pass

    def gbfsp(self,vertex, start=None, heuristic=lambda x,y:  y-x):
        """Greedy Best first search
        Comments: this is beging greedy on the distane you need to cover based on your current position. May not often work.
        This looks like a  illusion , is a good way to choose when only got one shot.
        """
        seen={}
        for v in self.vertices:
            seen[v]=False
        pq=[] #heapq
        #Initialize a priority queue of paths with the one-node path consisting of the initial state
        pq=[(0,([start or self.root],0))]
        #While (queue not empty)
        while pq:
            _,(path, pathcost)=heapq.heappop(pq)
            seen[path[-1]]=True
            if path[-1] is vertex:
                return path,pathcost
            else:
                for adj,costfunction in self.vertices[path[-1]].items():
                    if not seen[adj]:
                        newpath=path[::]
                        newpath.append(adj)
                        newpathcost =  pathcost + costfunction(path[-1], v )
                        heapq.heappush(pq, (heuristic(path[-1], vertex),(newpath, newpathcost)))

        return None

    def gbfhcsp(self, vertex, start=None, heuristic=lambda x,y:  y-x):
        """Greedy Best First Hill Climbing

        Comments: take the best heuristic available and go forward. most often you get the local minim, which is kind of like
        a local search for me.
        """
        seen={}
        for v in self.vertices:
            seen[v]=False
        #Initialize a priority queue of paths with the one-node path consisting of the initial state
        s=[([start or self.root],0)]
        #While (queue not empty)
        while s:
            #Remove path at root (which will be of min cost)
            path, pathcost=s.pop()
            seen[path[-1]]=True
            #If last node on path matches goal, return path
            if path[-1] is vertex:
                return path,pathcost
            #Else extend the path by one node in all possible ways, by generating successors of the last node on the path
            else:
                #Foreach successor path succ
                succesors=[]
                for adj,costfunction in self.vertices[path[-1]].items():
                    if not seen[adj]:
                        newpath=path[::]
                        newpath.append(adj)
                        newpathcost =  pathcost + costfunction(path[-1], v )
                        succesors.append((newpath,newpathcost))
                s+=sorted(succesors,key= lambda x: heuristic(x[0][-1],vertex), reverse=True)
        return None      

    def cycles(self,returnPath=False):
        """
        differentiate for directed and undirected graphs
        """
        pass

    def topologicalSort(self):
        pass
        # do a DFS

import random


"""
1->2,4
2->1,2,4,5
4->1,2,5
5->2,4,6
6->5
"""

g=graph(vertices=[1,2,3,4,5,6])
g.addAdjacency(1, [(2,lambda x,y:  1),(4,lambda x,y:  1)])
g.addAdjacency(2, [(1,lambda x,y:  1),(2,lambda x,y:  1),(4,lambda x,y:  1),(5,lambda x,y:  1)])
g.addAdjacency(4, [(1,lambda x,y:  1),(2,lambda x,y:  1),(5,lambda x,y:  1)])
g.addAdjacency(5, [(2,lambda x,y:  1),(4,lambda x,y:  1),(6,lambda x,y:  1)])
g.addAdjacency(6, [(5,lambda x,y:  1)])

print g.bfsp(6)
print g.dfsp(6) # depth first search
print g.ucsp(6) # uniform cost search
print g.gbfsp(6) # greedy best first search 
print g.gbfhcsp(6) # greedy best hill climbing search
