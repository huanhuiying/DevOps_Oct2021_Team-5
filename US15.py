#US15 - As a user, I want to be able to see my current score during each round to see 
# how much score I have accumulated to plan my next moves. (5)

grid = []

def loadGrid(grid,filename):
    file = open(filename, "r")
    for line in file:
        line = line.strip('\n')
        grid.append(list(line))
        
    return grid

grid = loadGrid(grid, "game_grid_testus15.csv")

def findType(loc, grid):
    column = [4, 10, 16, 22] #A, B, C, D
    row = [2, 4, 6, 8]
    for r in row:
        for c in column:
            lArray = [c, r]
            if loc == lArray:
                b = grid[r][c - 1] + grid[r][c] + grid[r][c + 1]
                print(b)
                if b == "BCH":
                    return "BCH"
                elif b == "FAC":
                    return "FAC"
                elif b == "HSE":
                    return "HSE"
                elif b == "HWY":
                    return "HWY"
                elif b == "SHP":
                    return "SHP"
                elif b == "   ":
                    return ""


def getBCHScore(loc):
    c = loc[0]
    if c == 4 or c == 22: # A or D
        return 3
    else:
        return 1

def getFACScoreArray(count):
    if(count == 1):
        return 1
    elif(count == 2):
        return [2, 2]
    elif(count == 3):
        return [3, 3, 3]
    elif(count == 4):
        return [4, 4, 4 ,4]
    elif(count > 4):
        cA = [4, 4, 4 ,4]
        remain = count - 4
        for i in range(remain):
            cA.append(1)
        return cA


