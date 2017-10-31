from collections import defaultdict 
d = defaultdict(list)
data = raw_input().split()
for i in range(int(data[0])):
    A = raw_input()
    d[A].append(str(i+1))
for j in range(int(data[1])):
    B = raw_input()
    print ' '.join(d[B]) or -1