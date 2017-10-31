from itertools import combinations
data = raw_input().split()
sorted_string = sorted(data[0])
n = int(data[1])
for i in range(1, n+1):
    for combination in combinations(sorted_string, i): 
        print ''.join(combination)