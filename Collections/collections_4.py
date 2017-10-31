from collections import OrderedDict
N = int(raw_input())
d = OrderedDict()

for item in range(N):
    data = raw_input().rsplit(' ', 1)
    if data[0] not in d:
        d[data[0]] = int(data[1])
    else:
        d[data[0]] += int(data[1])
for i in d:
    print i, str(d[i])