def merge_the_tools(string, k):
    L = []
    count = 0
    for i in string:
        count += 1
        if i not in L:
            L.append(i)
        if count == k:
            subString = ''.join(L)
            print subString
            L = []
            count = 0
    return subString