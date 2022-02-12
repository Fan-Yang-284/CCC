# Sunflowers

#handling input
lines = int(input())

sunflowers = []

for i in range(lines):
    line = input().split(" ")
    for i in range(len(line)):
        line[i] = int(line[i])
    sunflowers.append(line)

#function to rotate grid 90 deg
def rotateGrid(grid):
    grid = list(map(list, zip(*grid)))[::-1]
    return grid

#check if current grid is good top to bottom
def topBottom(sunflowers):
    for i in range(lines):
        heights = []
        for sunflower in sunflowers:
            heights.append(sunflower[i])
        if heights != sorted(heights):
            return False
    return True

#check if current grid is good left to right
def leftRight(sunflowers):
    for i in range(lines):
        if not sunflowers[i] == sorted(sunflowers[i]):   
            return False
    return True

while not topBottom(sunflowers) or not leftRight(sunflowers):
    sunflowers = rotateGrid(sunflowers)

for sunflower in sunflowers:
    for i in range(len(sunflower)):
        sunflower[i] = str(sunflower[i])
    print(" ".join(sunflower))