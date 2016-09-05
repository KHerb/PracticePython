import random
from random import randint
print "Welcome to guess a number 2.0 - This time I will try to guess a number that YOU pick in a range (0 - number)"
number = int(raw_input("What range would you like? (0 - ?) "))
def guess_game(number):
	guess = randint(0,number)
	new_list = [i for i in range(0,number+1)]
	validate = raw_input("Is your number %d? (y/n) " % guess)
	turn = 1
	while validate == 'n':
		turn += 1
		question = raw_input("Was my guess too high or too low? (high/low) ")
		if question == 'high':		 
			guess_list = [i for i in range(guess,number+1)]
			for i in guess_list:
				if i in new_list:
					new_list.remove(i)
			guess = random.choice(new_list)
			validate = raw_input("Is your number %d? (y/n) " % guess)
		elif question == "low":
			guess_list = [i for i in range(0,guess+1)]
			for i in guess_list:
				if i in new_list:		
					new_list.remove(i)
			guess = random.choice(new_list)
			validate = raw_input("Is your number %d? (y/n) " % guess)
	if validate == 'y':
		print "Impressive. It took me %d tries to get it right!" % turn
guess_game(number)


