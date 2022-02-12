from collections import Counter
height = int(input())
width = int(input())

numActions = int(input())

actions = []

for i in range(numActions):
    actions.append(input().split(" "))

grid = []
for i in range(height):
    grid.append([0]*width)

#even for black, odd for gold

for action in actions:
    num = int(action[1])-1
    if action[0] == "R":        
        for i in range(width):
            grid[num][i] +=1
    else:
        colNum = int(action[1])-1
        for i in range(height):
            grid[i][num] += 1

gold = 0

for i in range(height):
    for j in range(width):
        if grid[i][j] % 2 == 1:
            gold+=1

print(gold)