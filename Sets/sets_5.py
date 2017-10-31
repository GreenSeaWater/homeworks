n = input()
s = set(map(int, raw_input().split()))
commands = int(raw_input())
for x in range(commands):
    command = raw_input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print sum(s)