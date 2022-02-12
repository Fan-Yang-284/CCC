# Robothieves

from sys import stdin
from collections import defaultdict as dd
input = stdin.readline

h, w = map(int,input()[:-1].split(" "))

grid = []

camCells = set()
empty = set()
start = 0

for i in range(h):
    grid.append(list(input()[:-1])) # construct grid

adjDict = dd(list)

# get the neighbours for each cell (distance of one, adjacent)
def getNeighbours(i,j):
    res = []
    for a in range(i-1,i+2): #i-1,i,i+1
        for b in range(j-1,j+2): #j-1,j,j+1
            if abs(i-a) + abs(j-b) != 1:
                continue
            x,y = conveyors(a,b)
            if 0<x or x<h-1 and 0<y and y<=w-1:
                res.append((x,y))
    return res

def conveyors(a,b): # move one cell to correct destination cell using conveyors (getNeighbours helper)
    visited = set()
    while grid[a][b] == "W" or grid[a][b] == "U" or grid[a][b] == "L" or grid[a][b] == "D" or grid[a][b] == "R":
        if (a,b) in visited:
            return(-1,-1)
        visited.add((a,b))
        if grid[a][b]=="W":
            return (-1,-1)
        if grid[a][b]=="U":
            a-=1
        elif grid[a][b]=="D":
            a+=1
        elif grid[a][b]=="L":
            b-=1
        elif grid[a][b]=="R":
            b+=1
    return (a,b)

# loop through grid looking for empty squares, cameras
def handleGrid():
    global start
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "C":
                getCamCells(i,j)
            elif grid[i][j] == ".":
                empty.add((i,j))
            elif grid[i][j] == "S":
                start = (i,j)

def getCamCells(i,j): #get every cell seen by a camera, handleGrid helper
    x,y = i,j
    while x<h and grid[x][y]!="W": # going down
        camCells.add((x,y))
        x+=1
    x=i-1
    while x>=0 and grid[x][y]!="W": # going up
        camCells.add((x,y))
        x-=1
    x,y=i,j+1
    while y<w and grid[x][y]!="W":
        camCells.add((x,y))
        y+=1
    y=j-1
    while y>=0 and grid[x][y]!="W":
        camCells.add((x,y))
        y-=1
    
handleGrid()

for i in range(1,h-1):
    for j in range(1,w-1):
        if grid[i][j] == "W" or grid[i][j] == "U" or grid[i][j] == "L" or grid[i][j] == "D" or grid[i][j] == "R":
            continue
        adjDict[(i,j)] = getNeighbours(i,j) # construct adjacency list

BFS = [(start,0)]
ans = [[-1 for _ in range(w)] for _ in range(h)] # will store -1 in each cell
# by end, loop through ans, and print out values when cell is in empty set

#print(adjDict)

visited = set()

while BFS:
    #print(BFS)
    curr = BFS.pop(0)
    if curr[0] in visited:
        continue
    visited.add(curr[0])
    if curr[0] in camCells:
        continue
    
    if curr[0] in empty:
        ans[curr[0][0]][curr[0][1]] = curr[1]

    #print(adjDict[curr[0]])
    #print(curr[0])
    for cell in adjDict[curr[0]]:
        #print(cell)
        BFS.append((cell,curr[1]+1))


#printing out answer
for i in range(len(ans)):
    for j in range(len(ans[0])):
        if (i,j) in empty:
            print(ans[i][j])
