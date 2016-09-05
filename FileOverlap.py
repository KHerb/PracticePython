prime = "prime.txt"
happy = "happy.txt"
pin = open(prime,'r')
pnumber = [p.strip() for p in pin.readlines()]
pin.close()
hin = open(happy, 'r')
hnumber = [h.strip() for h in hin.readlines()]
hin.close()
overlap = []
for p in pnumber:
	if p in hnumber:
		overlap.append(p)
print "Here are the overlapping numbers -> " ,overlap