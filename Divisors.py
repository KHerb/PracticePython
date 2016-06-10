num = int(raw_input("Enter a number to return it's divisor: "))
lstrange = range(1,num+1)

def divisors(num):
	divisor = []
	for numbers in lstrange:
		if num % numbers == 0:
		    divisor.append(numbers)
	return divisor
print divisors(num)
