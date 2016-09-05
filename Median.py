#Median
def median(x):
	x.sort()
	for i in x:
		if len(x) % 2 != 0:
			return x[len(x)/2]
		elif len(x) == 1:
			return x[0]
		else:
			return float((x[len(x)/2] + x[len(x)/2 - 1])/2.0)

print median([1,2,3])

