def memo(f):
	cache={}
	def fun(*n):
		print len(cache)
		print [id(n) for i in n]
		key=hash(n)
		v=cache.get(key,False)
		if v:
			return v
		else:
			cache[key]=f(*n)
		return cache[key]
	return fun

@memo
def problem():
	pass
@memo
def fibonacci(n):
	return fibonacci(n-1)+fibonacci(n-2) if n>2 else 0 if n == 0 else 1

# print fibonacci(15)
# print fibonacci(10)

import random

seed=1
random.seed(seed)
matrices=[(random.randint(1,200),random.randint(1,200))]
for i in xrange(10):
	matrices.append((matrices[-1][1],random.randint(1,200)))
# print matrices


@memo
def cost(matrices,i):
	pass

@memo
def problem(inp,locale):
	matrices=inp
	l,r=locale
	lenm=r-l
	#Base case
	if lenm<1:
		return {"path":[],"cost":1}
	elif lenm == 1:
		return {"path":[(l,r)],"cost": matrices[l][0]*matrices[l][1]*matrices[r][0]}
	else:
		sol=[]
		for i in xrange(l,r):
			subproblem1=problem(matrices,(l,i))
			subproblem2=problem(matrices,(i+1,r))
			sol.append({"path":subproblem1["path"]+subproblem2["path"]+[(l,i,r) ],"cost":subproblem1["cost"]+subproblem2["cost"]+matrices[l][0]*matrices[l][1]*matrices[r][0]})
		return min(sol,key=lambda x:  x["cost"])
			
print problem(tuple(matrices), (0, len(matrices)-1))
