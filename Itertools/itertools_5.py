from itertools import groupby
string = raw_input()
modifiedString = []
for key, group in groupby(string):
    print (len(list(group)), int(key)),