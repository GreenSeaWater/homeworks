if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    L = []                                
    for i in range(n):
        L.append(integer_list[i])  
        t = tuple(L)
    print hash(t)