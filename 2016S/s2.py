from sys import stdin
input = stdin.readline
q = int(input())

n = int(input())

dmoj = sorted(list(map(lambda x: int(x),input()[:-1].split(" "))))
peg = sorted(list(map(lambda x: int(x),input()[:-1].split(" "))))

#print(dmoj)
#print(peg)

if q == 1:
    print(sum([max(dmoj[i],peg[i]) for i in range(n)]))
else:
    print(sum([max(dmoj[i],peg[n-i-1]) for i in range( n)]))