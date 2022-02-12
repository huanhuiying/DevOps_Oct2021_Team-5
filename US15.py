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
