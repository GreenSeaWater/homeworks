from collections import deque
N = int(raw_input())
d = deque()

for i in range(N):
    command = raw_input().split()
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    else:
        d.popleft()
for j in d: 
    print j,