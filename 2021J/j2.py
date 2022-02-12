# Silent Auction
lines = int(input())
max = 0
high = ""

for i in range(lines):
    name = input()
    price = int(input())
    if price > max:
        max = price
        high = name

print(high)
