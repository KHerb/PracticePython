num = int(raw_input("Enter a number to check if it is a prime number: "))
divisors = [x for x in range(2,num) if num%x==0]
if num == 1:
	print "This is NOT a prime number... by definition"
elif not divisors:
	print "This is a prime number."
else:
    print "This is NOT a prime number."