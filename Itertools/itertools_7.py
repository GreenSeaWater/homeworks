import itertools
K, M = map(int, raw_input().split())
L = []

for i in range(K):
    ar = list(map(int, raw_input().split()))
    L.append(ar[1:])
all_comb = itertools.product(*L)
result = 0
for j in all_comb:
    result = max(sum([x*x for x in j]) %M, result)
print result