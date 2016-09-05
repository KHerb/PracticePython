import random
lst = [i for i in range(random.randrange(0,1000))]
n = int(raw_input("Enter a number to see if it's in the list range: "))
def elementsearch(lst,n):
	if n in lst:
		return True
	else:
		return False
if elementsearch(lst,n) == True:
	print "%d is in the list range" % n
if elementsearch(lst,n) == False:
	print "%d is NOT in the list range" % n