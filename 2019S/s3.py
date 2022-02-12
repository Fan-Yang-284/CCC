#Arithmetic Squares

grid = []

for i in range(3):
    grid.append(input().split(" "))
    for j in range(len(grid[i])):
        if grid[i][j]!="X":
            grid[i][j] = int(grid[i][j])

def fill(): # looks through grid to check if any columns or rows have 2, then completes them accordingly
    changed = True

    while changed:
        changed = False
        for i in range(len(grid)): # rows
            xcount = 0
            for col in grid[i]:
                if col == "X":
                    xcount+=1
            if xcount == 1:
                complete(0,i) # fill the row
                changed = True  
        for i in range(3): # columns
            xcount = 0
            for row in grid:
                if row[i] == "X":
                    xcount+=1
            if xcount == 1:
                complete(1,i) #fill the column
                changed = True

def complete(type, i): # takes in type (row/col), which index
    if type == 0: # row has 2 numbers already
        if grid[i][0] == "X":
            grid[i][0] = grid[i][1] - (grid[i][2]-grid[i][1])
        elif grid[i][1] == "X":
            grid[i][1] = int((grid[i][2] + grid[i][0])/2)
        else:
            grid[i][2] = grid[i][1] + (grid[i][1]-grid[i][0])
    else: # column has 2 numbers already
        if grid[0][i] == "X":
            grid[0][i] = grid[1][i] - (grid[2][i]-grid[1][i])
        if grid[1][i] == "X":
            grid[1][i] = int((grid[2][i] + grid[0][i])/2)
        else:
            grid[2][i] = grid[1][i] + (grid[1][i]-grid[0][i])

fill()

def rotate(grid):
    return list(zip(*grid[::-1]))

for i in range(3): # print grid
    for j in range(3):
        grid[i][j] = str(grid[i][j])
    print(" ".join(grid[i]))