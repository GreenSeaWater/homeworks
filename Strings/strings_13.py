def minion_game(string):
    STUART_score = 0
    KEVIN_score = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            KEVIN_score += len(string) - i
        else:
            STUART_score += len(string) - i
    if KEVIN_score == STUART_score:
        print ('Draw')
    elif KEVIN_score > STUART_score:
        print ('Kevin'), KEVIN_score
    else:
        print ('Stuart'), STUART_score