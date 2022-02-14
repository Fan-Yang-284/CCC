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
        for i in range(3): # rows
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

def rotate(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0])-1,-1,-1)]

def getX():
    x = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "X":
                x+=1
    return x

def printGrid():
    for i in range(3): # print grid
        for j in range(3):
            grid[i][j] = str(grid[i][j])
        print(" ".join(grid[i]))

fill()

X = getX()
rotatecount = 0

while X!=0:
    if X == 4: # L shape, top right 2x2 square is empty
        while grid[0][2]!="X":
            grid = rotate(grid)
            rotatecount += 1
        if grid[1][1]!="X": # T shape turned 90 deg
            if grid[1][2]!="X":
                common = grid[1][2]-grid[1][1]
                for i in [0,2]:
                    for j in range(1,3):
                        grid[i][j] = grid[i][0]+j*common
            else: #upside down T
                common = grid[1][1]-grid[1][0]
                for i in range(2):
                    for j in [0,2]:
                        grid[i][j] = grid[j][2]-i*common
        else:
            common = grid[2][2] - grid[2][1]
            for i in range(2):
                for j in range(1,3):
                    grid[i][j] = grid[i][0]+j*common
    # any square with 5 missing becomes 4 missing (one row/col must have 2, which gets resolved with fill() )
    elif X == 6: # for 6 to be missing, either one row/col full, or 1 in each row, col
        while rotatecount<4 and grid[2][2] == "X":
            grid = rotate(grid)
            rotatecount+=1
        if rotatecount == 4: # middle column/row is all filled out
            if grid[1][0] != "X": # make it so that column is filled
                grid = rotate(grid)
                rotatecount = 1
            for i in range(3):
                found = False
                num = 0
                for j in range(3):
                    if grid[i][j]!="X":
                        num = grid[i][j]
                        found = True
                        break
                if found:
                    grid[i] = [num,num,num]
        elif grid[2][1] != "X" or grid[1][2] !="X": # bottom row or left col is filled out
            if grid[2][1] != "X":
                grid = rotate(grid)
                rotatecount+=1
                rotatecount%=4
            for i in range(3):
                found = False
                num = 0
                for j in range(3):
                    if grid[i][j]!="X":
                        num = grid[i][j]
                        found = True
                        break
                if found:
                    grid[i] = [num,num,num]
        else:
            if grid[1][1] == "X": # not diagonal
                grid[1][1] = grid[0][1]
            else:
                grid[0][1] = grid[1][1]
            fill()

    elif X == 7: # if 2 already in a row/col, must have been resolved already, so must be on diff row/col. this means we can just fill with given values
        for i in range(3):
            found = False
            num = 0
            for j in range(3):  
                if grid[i][j]!="X":
                    num = grid[i][j]
                    found = True
                    break
            if found:
                grid[i] = [num,num,num]
                
        # up to this point two rows have been filled
        fill()        
    elif X == 8: # only 1 value, fill with given value
        num = 0
        for i in range(3):
            end = False
            for j in range(3):
                if grid[i][j] != "X":
                    num = grid[i][j]
                    end = True
                    break
            if end:
                break
        for i in range(3):
            for j in range(3):
                grid[i][j] = num
    elif X == 9:
        grid = [[0]*3 for _ in range(3)]

    X = getX()

for i in range(4-rotatecount):
    grid = rotate(grid)

printGrid()