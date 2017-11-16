import csv

def build_inverted_index(filename,keyindex,textindex):
    csv_reader =csv.reader(open(filename))
    d={}
    for line in csv_reader:
        document = line[keyindex]
        textstring = line[textindex]
        # cleantext = "".join([x if x.isalpha() else ' ' for x in s ])
        cleantext = ""
        for letter in textstring:
            if letter.isalpha():
                cleantext = cleantext + letter
            else:
                cleantext = cleantext + " "
        wordlist = cleantext.split()
        for word in wordlist:
            d.setdefault(word,[])
            d[word].append(document)
    return d

sample_index = build_inverted_index('sample-texts.csv',0,1)
texas_index = build_inverted_index('offenders-clean.csv',0,8)
build_inverted_index("sample-texts.csv",0,1)
