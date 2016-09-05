AA = {'LYS':'K', 'ALA':'A', 'ARG':'R', 'ASN':'N', 'ASP':'D','CYS':'C','GLU':'E', 'GLY':'G','HIS':'H', 'ILE':'I','LEU':'L','MET':'M', 'PHE':'F', 'PRO':'P', 'SER':'S', 'THR':'T', 'TRP':'W', 'TYR':'Y','VAL':'V','GLN':'Q'}
print 'Amino Acid Sequence differences\n'.center(60,' ')
s1=''
s2=''
with open(str(raw_input("Enter name of pdb file (name.pdb): ")),'r') as pdb1:
	for line in pdb1:
		if 'SEQRES' in line:
			if ' A ' in line:
				for word in line.split():
					for i in AA.keys():
						if word == i:
							s1 += AA.get(word)
with open(str(raw_input("Enter name of the second pdb file (name.pdb): ")),'r') as pdb2:
	for line in pdb2:
		if 'SEQRES' in line:
			if ' A ' in line:
				for word in line.split():
					for i in AA.keys():
						if word == i:
							s2 += AA.get(word)
def sequences(s1,s2):
	length = len(s1)
	lengthi = [int(i) for i in range(0,length)]
	nomatch = []
	for i in lengthi:
		if s1[i] != s2[i]:
			nomatch.append(i)
	return nomatch
def substitutions(nomatch):
	for i in nomatch:
		print "Amino Acid: %s%d substituted for %s%d" % (s1[i], i+1, s2[i], i+1)
	print "Total Amino Acid Substitutions:",len(nomatch)
def Rgroups(nomatch):
	polar = 'STCYNQ'
	non_polar = 'GAVLIMFWP'
	acid = 'ED'
	base = 'KRH'
	aromatic = 'WFY'
	for i in nomatch:
		if s1[i] in polar and s2[i] not in polar:
			if s2[i] in aromatic:
				print "Amino Acid %s%d is POLAR and has been substituted for %s%d which has an AROMATIC R-group" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in acid:
				print "Amino Acid %s%d is POLAR and has been substituted for %s%d, a POLAR aa with an ACIDIC R-group" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in non_polar:
				print "Amino Acid %s%d is POLAR and has been substituted for %s%d, a NON-POLAR aa" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in base:
				print "Amino Acid %s%d is POLAR and has been substituted for %s%d, a POLAR aa with a BASIC R-group" % (s1[i], i+1, s2[i], i+1)
		elif s1[i] in non_polar and s2[i] not in non_polar:
			if s2[i] in aromatic:
				print "Amino Acid %s%d is NON-POLAR and has been substituted for %s%d which has an AROMATIC R-group"% (s1[i], i+1, s2[i], i+1)
			elif s2[i] in acid:
				print "Amino Acid %s%d is NON-POLAR and has been substituted for %s%d, a POLAR aa with an ACIDIC R-group"% (s1[i], i+1, s2[i], i+1)
			elif s2[i] in base:
				print "Amino Acid %s%d is NON-POLAR and has been substituted for %s%d, a POLAR aa with a BASIC R-group" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in polar:	
				print "Amino Acid %s%d is NON-POLAR and has been substituted for %s%d, a POLAR aa" % (s1[i], i+1, s2[i], i+1)
		elif s1[i] in aromatic and s2[i] not in aromatic:
			if s2[i] in base:
				print "Amino Acid %s%d is AROMATIC and has been substituted for %s%d, a POLAR aa with a BASIC R-group" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in acid:
				print "Amino Acid %s%d is AROMATIC and has been substituted for %s%d, a POLAR aa with an ACIDIC R-group" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in non_polar:
				print "Amino Acid %s%d is AROMATIC and has been substituted for %s%d, a NON-POLAR aa"  % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in polar:
				print "Amino Acid %s%d is AROMATIC and has been substituted for %s%d, a POLAR aa" % (s1[i], i+1, s2[i], i+1)	
		elif s1[i] in base and s2[i] not in base:
			if s2[i] in aromatic:
				print "Amino Acid %s%d is BASIC and has been substituted for %s%d which has an AROMATIC R-group " % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in acid:
				print "Amino Acid %s%d is BASIC and has been substituted for %s%d, a POLAR aa with an ACIDIC R-group" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in non_polar:
				print "Amino Acid %s%d is BASIC and has been substituted for %s%d, a NON-POLAR aa"  % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in polar:
				print "Amino Acid %s%d is BASIC and has been substituted for %s%d, a POLAR aa" % (s1[i], i+1, s2[i], i+1)
		elif s1[i] in acid and s2[i] not in acid:	
			if s2[i] in aromatic:
				print "Amino Acid %s%d is ACIDIC and has been substituted for %s%d which has an AROMATIC R-group " % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in base:
				print "Amino Acid %s%d is ACIDIC and has been substituted for %s%d, a POLAR aa with a BASIC R-group" % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in non_polar:
				print "Amino Acid %s%d is ACIDIC and has been substituted for %s%d, a NON-POLAR aa"  % (s1[i], i+1, s2[i], i+1)
			elif s2[i] in polar:
				print "Amino Acid %s%d is ACIDIC and has been substituted for %s%d, a POLAR aa" % (s1[i], i+1, s2[i], i+1)
		else:
			print "Amino Acid %s%d has been substituted for %s%d with an equally functioning R-Group" % (s1[i], i+1, s2[i], i+1)

substitutions(sequences(s1,s2))
print
Rgroups(sequences(s1,s2))
