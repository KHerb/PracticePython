with open('words.txt','r') as word:
	words = [w.strip() for w in word.readlines()]
#1.  Sort the list of words alphabetically by their *backwards* spelling.
    #(Example: 'aa', 'baa', 'markkaa', 'ba', 'aba', 'baba' ... )
back = [w[::-1] for w in words]
back.sort()
front = [w[::-1] for w in  back]

#2.  Compute the distribution of word lengths.  What are the longest words in this dictionary?
import numpy as np
length = [len(w) for w in words]
length.sort()
maxlength = int(length[-1])
counts, bins = np.histogram((length), bins=range(maxlength+2))
for i in range(maxlength+1):
	print i, counts[i]
Ind = np.argsort([-len(w) for w in words])[0:3]  # top 3
three_longest = np.array(words)[Ind]
print three_longest
#3.  Which pairs of letters are the most statistically over-represented in English words?  Rank all pairs of letters
    #x and y by the quantity P(x,y)/[P(x)P(y)].
letters = list('abcdefghijklmnopqrstuvwxyz')
n_single = {}   # {'a': counts, ....}
n_double = {}   # {'a':{'b': counts}}
for letter in letters:
    print 'getting frequency counts for:',  letter
    n_single[letter] = sum([w.count(letter) for w in words])
    n_double[letter] = {}
    for letter2 in letters:
        n_double[letter][letter2] = sum([w.count(letter+letter2) for w in words])

# Normalize the single-letter distribution
print 'n_single', n_single
total_single = sum([n_single[k] for k in n_single.keys()])
print 'total_single', total_single
p_single = {}
for k in n_single.keys():
    p_single[k] = float(n_single[k])/float(total_single)

# Normalize the double-letter distribution
print 'n_double', n_double
total_double = 0  
for k in n_double.keys():
    total_double += sum([n_double[k][l] for l in n_double[k].keys()]) 
print 'total_double', total_double
p_double = {}
for k in n_double.keys():
    p_double[k] = {}
    for l in n_double[k].keys():
        p_double[k][l] = float(n_double[k][l])/float(total_double)

pairs = []         
ranks = []    # P(k,l)/[P(k)P(l)]
for k in letters:
  for l in letters:
      pairs.append( k+l )
      ranks.append( p_double[k][l]/(p_single[k]*p_single[l]) )
Ind_sorted = np.argsort(-np.array(ranks))
print '#pair\tP(k,l)/[P(k)P(l)]'
for i in Ind_sorted:
    print pairs[i], ranks[i]
#4.  How many pairs of words share a consecutive string of at least four letters?  HINT: remember to avoid self-counting
   #(word i vs. i) and symmetric pairs (i,j) versus (j,i)
def find_overlapping_pairs(words, n=4):
    """Find how many pairs of words share a consecutive string of at least n letters."""
    pairs = [] 
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if overlap(words[i], words[j]) >= n:
                print words[i], words[j]
                pairs.append( (words[i], words[j]) )
    return pairs
        

def overlap(s1, s2):
    """Find the length of the largest overlapping substring between string s1 and string s2"""

    maxlength  = 0
    for sublength in range(1,len(s1)+1):
        substrings = [s1[i:i+sublength] for i in range(len(s1)-sublength+1)]
        #print 'sublength', sublength, 'substrings', substrings

        for s in substrings:
            if s2.find(s) >= 0:  # returns index if found, returns -1 if not found
                maxlength = sublength
                break     
        #print 'maxlength', maxlength
    return maxlength
   
#overlap('abracadabra', 'candelabra')
find_overlapping_pairs(words, n=4)
