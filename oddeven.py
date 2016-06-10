user = raw_input("Enter a number and I will tell you if it's Odd or Even: ")
user = int(user)
if user % 4 == 0:
	print "multiple of four and Even"
elif user % 2 == 0:
	print "Even"
else:
	print "Odd"