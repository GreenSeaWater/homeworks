from itertools import permutations
data = raw_input().split()
sorted_word = sorted(data[0])
for permutation in list(permutations(sorted_word, int(data[1]))):  #leva list
    print ''.join(permutation)