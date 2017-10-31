if __name__ == '__main__':
    n = int(raw_input())
    d = {}
    for _ in range(n):
        line = raw_input().split()
        name = line[0]
        individualMarks = line[1:]
        sumMarks = 0
        for score in individualMarks:
            sumMarks += float(score)
            average = sumMarks/3.0
            d[name] = "%.2f" % average
    userName = raw_input()
    print d[userName]