from itertools import product
A = map(int, raw_input().split())
B = map(int, raw_input().split())
print ' '.join(map(str, product(A,B)))