# Crazy Fencing
pieces = int(input())
heights = input().split(" ")

for i in range(len(heights)):
    heights[i] = int(heights[i])

widths = input().split(" ")
for i in range(len(widths)):
    widths[i] = int(widths[i])

counter = 0
area = 0

while counter<len(heights)-1:
    area+=(heights[counter]+heights[counter+1])*widths[counter]/2
    counter+=1

print(area)