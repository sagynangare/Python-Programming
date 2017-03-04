from collections import Counter
x, size, n, money = input(), Counter(map(int, raw_input().split())), input(), 0
for i in range(n):
    cus = map(int, raw_input().split())
    if size[cus[0]] > 0 :
        money += cus[1]
        size[cus[0]] = size[cus[0]] -1
print money
