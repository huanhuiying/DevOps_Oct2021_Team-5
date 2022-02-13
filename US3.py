import ast

grid = []

#function to load game map
#function implemented in previous sprint
def load_file(grid,filename):
    file = open(filename, "r")
    for line in file:
        line = line.strip('\n')
        grid.append(list(line))
        
    return grid

def load_saved_game(grid):
    gridFile = "savecontent/savefile.csv"
    grid = load_file(grid, gridFile)

    buildingFile = "savecontent/buildingCount.csv"
    no_buildings = open(buildingFile, "r")
    no_buildings = no_buildings.read()
    no_buildings = ast.literal_eval(no_buildings)

    turnFile = "savecontent/turncount.csv"
    turn_counter = open(turnFile, "r")
    turn_counter = int(turn_counter.read())

    return grid, no_buildings, turn_counter
    
    
    
