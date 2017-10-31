A = set(raw_input().split())
set_number = input()
result = True
for item in range(set_number):
    B = set(raw_input().split())
    if not A.issuperset(B):
        result = False
print result