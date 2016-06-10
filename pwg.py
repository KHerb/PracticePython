import random
def pwgenerator():
	lower = 'abcdefghijklmnopqrstuvwxyz'
	up = lower.upper()
	special = "~!@#$%^&*()_-+=}{|[]\?/:;'<>,."
	password = ""
	for i in range(3):
		password += random.choice(lower)
		password += random.choice(up)
		password += random.choice(special)
	return password
pwg = pwgenerator()
print "Welcome to Password Generator 1.0!\nHere is your temporary password:" ,pwg

def password():
	print "Your new password must be at least 9 characters long."
	x = raw_input("Enter your password: ")
	z = '1234567890'
	for i in x:
		while len(x) < 9 and i not in z:
			x = raw_input("Enter your password again: ")
	else:
		print "Your password has been changed to '%s', Thank you." % x
		return x

personal = raw_input("Would you like to change your password? (y/n) ")
while personal != 'y' and personal != 'n':
	personal = raw_input("Sorry, what was that? (y/n)")
if personal == 'y':
	password()
elif personal == 'n':
	print "Your password will still be " ,pwg + " the next time you log in"