a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list(set([x for x in a for y in b if x == y]))
print c

#for random list generation!
"""import random
a, b = random.sample(range(100),10), random.sample(range(100),10)
c = list(set([x for x in a for y in b if x == y]))
print "Random list A: %s" % a
print "Random list B: %s" % b
print "Common numbers: %s" % c"""