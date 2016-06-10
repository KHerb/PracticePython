from random import randint
print "Welcome to guess a number. Type '0' anytime to stop playing."
def guess_game():
    guess = int(raw_input("Guess a number between 1 and 9: "))
    randnum = randint(1,9)
    turn = 1	
    while guess != randnum:
    	if guess == 0 or guess == randnum:
    	    break
        elif guess > randnum:
	        guess = int(raw_input("You guessed too high! Guess again: "))
	        turn += 1
        elif guess < randnum:
		    guess = int(raw_input("You guessed too low! Guess again: "))
		    turn += 1

    if guess == randnum:
        print "The number was %d. It took you %d tries to get it right!" % (randnum, turn)
    else:
    	print "Never give up..."
guess_game()
