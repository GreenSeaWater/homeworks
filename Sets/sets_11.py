K = input()
room_number_LIST = list(map(int, raw_input().split()))
room_number_SET = set(room_number_LIST)
list_SUM = sum(room_number_LIST)
set_SUM = sum(room_number_SET) * K
difference = set_SUM - list_SUM
for item in room_number_SET:
    if difference == (K-1) * item:
        print item