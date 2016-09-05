x = map(int, raw_input("Enter numbers seperated by spaces to return a list less than 5: ").split()) 
# map built-in function takes two arguments: map applies int function to all numbers input by user, after it splits user input into individual items of a list
# the user input is now a list of numbers, which can then be manipulated to return numbers less than 5.
y = []
for i in x:
	if i < 5:
		y.append(i)
print y