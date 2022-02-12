# Swapping seats
from collections import Counter

line = input()

letters = dict(Counter(line))
numA = letters['A']
numB = letters['B']

backlen = backleng = 0

j = k = len(line) - 1

while line[j]=='A':
    backlen+=1
    j-=1

counter1 = counter2 = 0

for i in range(numA - backlen):
    if line[i] == 'B':
        counter1+=1

while line[k]=='B':
    backleng+=1
    k-=1

for i in range(numB - backleng):
    if line[i] == 'A':
        counter2+=1

counter = min(counter1,counter2)

print(counter)