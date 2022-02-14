# Sum Game
from sys import stdin
input = stdin.readline
res = 0

N = int(input()[:-1])

l1 = list(map(int,input()[:-1].split(" ")))
l2 = list(map(int,input()[:-1].split(" ")))

sum1,sum2 = 0,0

for i in range(N):
    sum1+=l1[i]
    sum2+=l2[i]
    if sum1==sum2:
        res = i+1

print(res)
