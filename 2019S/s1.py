#Flipper
line = list(input())

grid = [1,2,3,4]

for c in line:
    if c == "H":
        grid[0], grid[2] = grid[2], grid[0]
        grid[1], grid[3] = grid[3], grid[1]
    if c == "V":
        grid[0], grid[1] = grid[1], grid[0]
        grid[2], grid[3] = grid[3], grid[2]

print(str(grid[0]) + " " + str(grid[1]))
print(str(grid[2]) + " " + str(grid[3]))