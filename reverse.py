
x = str(raw_input("Type a sentence and I will reverse the order of it! "))
def reverse(x):
	x = x.split(" ")
	for i in x:
		f = x[::-1]
		f = " ".join(f)
	return f
print reverse(x)




