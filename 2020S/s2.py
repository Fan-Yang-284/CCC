# Escape Room
from sys import stdin
input = stdin.readline

height = int(input()[:-1])
width = int(input()[:-1])
grid = []
targetPair = (height,width)
neededNum = height*width #need to go from cell with this value to land on target cell

dp = [[] for i in range(10**6+1)] #memoize

def factorize():
    for i in range(1,height+1):
        for j in range(1,width+1):
            dp[i*j].append((i,j))

factorize()
#print(dp)
exists = False

for i in range(height):
    line = input()[:-1].split(" ")
    for j in range(len(line)):
        line[j] = int(line[j])
        if line[j] == neededNum: #see if any cell can lead to target
            exists = True
    grid.append(line)

if not exists:
    print("no")

else:
    visited = set()
    factors = dp[grid[0][0]] #get all factor pairs of starting cell value
    found = False

    while factors:
        curr = factors.pop(0)
        if curr == targetPair: # check for success
                print("yes")
                found = True
                break
        if curr in visited:
            continue
        visited.add(curr)

        if curr[0]<=height and curr[1]<=width: # within bounds
            factors+=dp[grid[curr[0]-1][curr[1]-1]]

    if not found:
        print("no")