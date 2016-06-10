print "Welcome to Rock, Paper, Scissors!"
ready = raw_input("Requires two players; Are you ready to play? (y/n) ")
while ready != 'y' and ready != 'n':
	ready = raw_input("Oops, I didn't quite get that.")

def player_1():
	 x = raw_input("Player 1 - Pick your mode of attack! ")
	 while x != 'Rock'and x !='rock' and x != 'Paper'and x != 'paper'and x != 'scissors'and x !='Scissors':
	     x = raw_input("Oops, that won't do you any good... ")
	 return x

def player_2():
	x = raw_input("Player 2 - Pick your mode of attack! ")
	while x != 'Rock'and x != 'rock'and x != 'Paper'and x != 'paper'and x != 'scissors'and x != 'Scissors':
		x = raw_input("Oops, that won't do you any good... ")
	return x 
def play_again():
	play_again = raw_input("Would you guys like to play again? (y/n) ")
	while play_again != 'y' and play_again != 'n':
	    play_again = raw_input("I'm sorry, what was that? (y/n) ")
        if play_again == 'y':
	        return check()
        elif play_again == 'n':
	        print "Thanks for playing!"
 
def check():
	Score1 = 2
	Score2 = 2
	while Score1 > 0 and Score2 > 0:
	    P1 = player_1()
	    P2 = player_2()
	    if P1.lower() == P2.lower():
	        print "it's a tie!"
	    elif P1.lower() == "rock" and P2.lower() == "scissors":
		    print "Player 1 Wins!"
		    Score1 -= 1
	    elif P1.lower() == "paper" and P2.lower() == "rock":
	        print "Player 1 Wins!"
	        Score1 -= 1
	    elif P1.lower() == "scissors" and P2.lower() == "paper":
		    print "Player 1 Wins!"
		    Score1 -= 1
	    else:
		    print "Player 2 Wins!"
		    Score2 -= 1

	    if Score1 == 0:
		    print "Congratulations Player 1 for winning best out of three!"
        if Score2 == 0:
		    print "Congratulations Player 2 for winning best out of three!"
	play_again()	    
check()  