import random
from sys import exit
x = str(random.randint(1000,9999))

def cows_and_bulls():
	user = raw_input("What is your guess? ")
	Bulls,Cows,guess = 0,0,1
	while user != x:
		guess += 1
		for i in range(len(user)):
			if user[i] == x[i]:
				Cows += 1
			elif user[i] in x:
				Bulls += 1
		print "%s Cows, %s Bulls" % (Cows,Bulls)
		user = raw_input("Guess again ")
		Bulls,Cows = 0,0
	else:
		print "You won! The number was %s and it took %s guess(es)!" % (x, guess)

if __name__ == "__main__":
	print "Welcome to the 'Cows and Bulls' game! -  You will be required to guess the\ncorrect order of numbers of a randomly generated 4-digit number.\nA 'Cow' will be given if you guessed a right number in the right place. A 'Bull'will be given if the number is correct but in the wrong place." 
	ready = raw_input("Are you ready to play? (y/n) ")
	while ready != 'y' and ready != 'n':
		ready = raw_input("Are you ready? (y/n)")
	if ready == 'n':
		exit()
	elif ready == 'y':
		cows_and_bulls()