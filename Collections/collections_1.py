X = int(raw_input())
shoe_size = map(int, raw_input().split())
N = int(raw_input())    
money = 0

for customer in range(N):
    purchase_order = map(int, raw_input().split())
    if purchase_order[0] in shoe_size:
        money += purchase_order[1]
        shoe_size.remove(purchase_order[0])
print money
