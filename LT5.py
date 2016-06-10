lst = [int(x) for x in raw_input("Enter a list of numbers seperated by spaces to return that list for numbers less than 5: ").split() if int(x) < 5]
print lst