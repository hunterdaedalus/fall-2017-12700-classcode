import csv


def reader():
    mydict = {}
    with open('sample-texts.csv') as csvfile:
        readstuff = csv.reader(csvfile)
        for row in readstuff:
            row[1] = row[1].split()
            for word in row[1]:
                mydict[word] = []
            for k, v in mydict.iteritems():
                for word in row[1]:
                    if k == word:
                        v = v.append(row[0])
    return mydict


print(reader())
