user = raw_input("Enter a word and I will check if it is a palindrome or not: ")
if user[::-1] == user:
	print "The word '%s' is a palindrome." % (user)
else:
	print "The word '%s' is NOT a palindrome." % (user)