# Modern Art
from collections import Counter
height = int(input())
width = int(input())

numActions = int(input())

actions = []

for i in range(numActions):
    line = input().split(" ")
    line = line[0]+line[1]
    actions.append(line)

actions = dict(Counter(actions))
newActions = list(actions.keys())

numR = 0
numC = 0
numGold = 0

for action in newActions:
    if actions[action]%2==0:
        continue
    if action[0] == "R":
        numR += 1        
        numGold += (width - numC*2)
    else:
        numC +=1
        numGold += (height - numR*2)

print(numGold)
