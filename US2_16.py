from numpy import append


def save_game(grid):
    fileName = "savecontent/savefile.csv"
    file=open(fileName,'w')
    export_map = []
    for i in range (len(grid)):
        temp = ''
        for j in range(len(grid[i])):
            temp += grid[i][j]
        export_map.append(temp)
    
    for h in range(len(export_map)):
        file.write('{}\n'.format(export_map[h]))
    print("Your progress has been saved!")
    return export_map

def save_building(no_buildings):
    buildingFile = "savecontent/buildingCount.csv"
    file=open(buildingFile,'w')
    for count, value in no_buildings.items():
        file.write('%s: %s\n' % (count,value))
    return (no_buildings)

def save_turnCount(turncount):
    fileName = "savecontent/turncount.csv"
    file=open(fileName, 'w')
    turncount = str(turncount)
    file.write(turncount)
    return turncount

def save_points(hseArray, facArray, shpArray, hwyArray, bchArray):
    fileName = "savecontent/scoresave.csv"
    file=open(fileName,'w')
    # hseArray = list(hseArray)
    # facArray = list(facArray)
    # shpArray = list(shpArray)
    # hwyArray = list(hwyArray)
    # bchArray = list(bchArray)
    scoreArray = scoreArray.append(hseArray, facArray, shpArray, hwyArray, bchArray)
    export_score = []
    for i in range (len(scoreArray)):
        temp = ''
        for j in range(len(scoreArray[i])):
            temp += scoreArray[i][j]
        export_score.append(temp)
    
    for h in range(len(export_score)):
        file.write('{}\n'.format(export_score[h]))
    return scoreArray