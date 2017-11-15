import random

def remove_non_alpha(w):
    """
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    """
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
    for i in range(1,len(wordlist)):
        w1 = wordlist[i-1]
        w2 = wordlist[i]
        d.setdefault(w1,[])
        d[w1].append(w2)
        
    return d

def build_trigram_dict(wordlist):
    d = {}
    for i in range(0,len(wordlist)-2):
        # a = wordlist[i]
        # b = wordlist[i+1]
        # c = wordlist[i+2]
        (a,b,c) = (wordlist[i],wordlist[i+1],wordlist[i+2])
        tuple = (a,b)
        d.setdefault(tuple,[])
        d[tuple].append(c)
    return d

def build_ngrams(wordlist,prelength):
    d = {}
    for i in range(0,len(wordlist)-prelength):
        sublist = wordlist[i:i+prelength+1]
        t = tuple(sublist[0:len(sublist)-1])
        d.setdefault(t,[])
        d[t].append(sublist[-1])
    return d
        

def bwcff(f,prelength):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of the number of times each word occursb
    """
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = build_ngrams(l,prelength)
    return d

# def generate_text(d,start_word,length=50):
#     wordlist = []
#     next = start_word
#     for i in range(length):
#         if next not in d:
#             break
#         wordlist.append(next)
#         next = random.choice(d[next])
#     return " ".join(wordlist)

def generate_text(d,length=50):
    k = d.keys()
    key_list = list(k)
    next = random.choice(key_list)
    text_list = list(next)
    for i in range(length):
        new_word = random.choice(d[next])
        if new_word == "":
            break
        next = next[1:] + (new_word,)
        text_list.append(new_word)
    return " ".join(text_list)


        
    



h1 = bwcff("hamlet.txt",1)
p1 = bwcff("psalms.txt",1)
s1 = bwcff("sonnets.txt",1)

h2 = bwcff("hamlet.txt",2)
p2 = bwcff("psalms.txt",2)
s2 = bwcff("sonnets.txt",2)

h3 = bwcff("hamlet.txt",3)
p3 = bwcff("psalms.txt",3)
s3 = bwcff("sonnets.txt",3)
