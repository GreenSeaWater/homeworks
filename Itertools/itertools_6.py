from itertools import combinations
N = int(raw_input())
L = raw_input().split()
K = int(raw_input())

all_comb= list(combinations(L, K))
valid_comb = 0
for i in all_comb:
    if 'a' in i:
        valid_comb += 1
print valid_comb/float(len(all_comb))