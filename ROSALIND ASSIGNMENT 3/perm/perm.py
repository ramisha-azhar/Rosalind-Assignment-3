import re
import math
import itertools

def perm(n):
	print (str(math.factorial(n)))
	totalPerm = math.factorial(n)
	perms=itertools.permutations(range(1,n+1))
	line = ""
	for a in perms:
		for i in a:
			line = line + " " +str(i)

		line = re.sub('^ ','',line)
		print (line)
		line = ""

perm(5)
