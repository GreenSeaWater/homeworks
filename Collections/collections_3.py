from collections import namedtuple
N = int(raw_input())
STUDENT = namedtuple('STUDENT', raw_input().split())
total_marks = 0
for i in range(N):
    data = raw_input().split()
    std = STUDENT(data[0], data[1], data[2], data[3])
    total_marks += float(std.MARKS)
print total_marks/N