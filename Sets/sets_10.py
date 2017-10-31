n = input()
A = set(map(int, raw_input().split()))
set_number = input()

for item in range(set_number):
    command = raw_input().split()
    B = set(map(int, raw_input().split()))
    if command[0] == 'update':
        A.update(B)
    elif command[0] == 'intersection_update':
        A.intersection_update(B)
    elif command[0] == 'difference_update':
        A.difference_update(B)
    elif command[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
print sum(A)