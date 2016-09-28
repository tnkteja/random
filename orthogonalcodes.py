from __future__ import division

def dotproduct(X,Y):   return int(sum(map(lambda x,y:  x*y,X,Y))/len(X))
A=(-1,-1,-1,1,1,-1,1,1)
negation = lambda X:  [ 1 if i < -1 else 1 for i in X]
Ad = negation(A)
 
print dotproduct(A,A)

B=(-1,-1,1,-1,1,1,1,-1)

print dotproduct(A,negation(B))
print dotproduct(A,B)
print dotproduct(A,negation(A))
