if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    no_repetitions = set(arr)             
    final_arr = list(no_repetitions)
    final_arr.sort()
    print final_arr[-2]