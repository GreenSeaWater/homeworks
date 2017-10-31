from itertools import combinations_with_replacement
data = raw_input().split()
sorted_string = sorted(data[0])
for item in combinations_with_replacement(sorted_string, int(data[1])):
    print ''.join(item)