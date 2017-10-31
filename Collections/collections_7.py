from collections import deque
test_cases = int(raw_input())
for test in range(test_cases):
    n = int(raw_input())
    sideLengths = deque(map(int, raw_input().split()))
    for i in range(n-1):
        if sideLengths[0] >= sideLengths[1]:
            sideLengths.popleft()
        elif sideLengths[-1] >= sideLengths[-2]:
            sideLengths.pop()
    print 'No' if len(sideLengths) > 1 else 'Yes'