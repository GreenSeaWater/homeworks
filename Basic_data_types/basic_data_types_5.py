N = int(raw_input())
lst = []
ListOfScores = []
for _ in range(N):
    name = raw_input()
    score = float(raw_input())
    
    ListOfScores.append(score)
    lst.append([name, score])
lst.sort()
NoRepetition = list(set(ListOfScores))
NoRepetition.remove(min(NoRepetition))
for x in range(N):
    if lst[x][1] == min(NoRepetition):
        print lst[x][0]