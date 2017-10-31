M = input()
M_set = set(map(int, raw_input().split())) 
N = input()
N_set = set(map(int, raw_input().split()))
for i in sorted(M_set ^ N_set):
    print i