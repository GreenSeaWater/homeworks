from collections import OrderedDict
n = int(raw_input())
d = OrderedDict()
for i in range(n):
    word = raw_input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print len(d)
for i in d.values():
    print i,