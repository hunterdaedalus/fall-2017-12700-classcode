import random

def rp(w):
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def bwcd(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d
    
def build_word_chain_dict(wordlist):
    d={}
    for i in range (1,len(wordlist)):
        w1 = wordlist[i-1]
        w2 = wordlist[i]
        d.setdefault(w1,[])
        d[w1].append(w2)
        #d[w] = d[w] + 1
    return d

def bwcff(f):
    f = open(f).read()
    l=[]
    for w in f.split():
        w = w.lower()
        w = rp(w)
        l.append(w)
    d = build_trigram_dict(l)
    return d

def generate_text(d,start_word,length=50): # how many words we want this text to be, and the first word of text
    wordlist = []
    next = start_word
    for i in range(length):
        if next not in d:
            break
        wordlist.append(next)
        next = random.choice(d[next])
    return " " . join(wordlist)

def build_trigram_dict(wordlist):
    d = {}
    for i in range(0,len(wordlist)-2): #why did this happen
       # a = wordlist[0]
       # b = wordlist[1]
       # c = wordlist[2]
       (a,b,c) = (wordlist[0],wordlist[1], wordlist[2])
       tuple = (a,b)
       d.setdefault(tuple,[])
       d[tuple].append(c)
    return d

def build_ngrams(worldlist,prelength):
    d = {}
    for i in range(0,len(wordlist)-prelength):
        sublist = wordlist[i:i+prelength]
        t = tupile(sublist[0:len(sublist)-1])

hamlet = bwcff("hamlet.txt")
psalms = bwcff("psalms.txt.")

#d = bwcff("hamlet.txt")
#print(bwcff("hamlet.txt"))