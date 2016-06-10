from random import sample
b =['Dog','Dog','Cat']
a = sample(range(100),10)
def rem_dup(x): #Any list can be passed through this to remove duplicates
	for i in x:
		if x.count(i) > 1:
			x.remove(i)
	return x
print rem_dup(a)
print rem_dup(b) # just to check if it works!