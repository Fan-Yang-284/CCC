# What is N

N = int(input())

res = 0

for i in range(1,6):
    j = N-i
    if j>=0 and j<=5 and i>=j:
        res+=1

print(res)