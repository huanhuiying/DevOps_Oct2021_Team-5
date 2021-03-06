#US15 - As a user, I want to be able to see my current score during each round to see 
# how much score I have accumulated to plan my next moves. (5)

#US19 - As a user, I want to be able to see the computation of the final score 
# so that I can understand how the points are calculated. 

def loadGrid(grid,filename):
    file = open(filename, "r")
    for line in file:
        line = line.strip('\n')
        grid.append(list(line))
        
    return grid

def findType(loc, grid):
    column = [4, 10, 16, 22] #A, B, C, D
    row = [2, 4, 6, 8]
    for r in row:
        for c in column:
            lArray = [c, r]
            if loc == lArray:
                b = grid[r][c - 1] + grid[r][c] + grid[r][c + 1]
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
    if(count == 0): #added code 
        return 0 #added code 
    elif(count == 1):
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

def getFACTotalScore(a):
    count = 0
    for i in a:
        count = count + i
    return count

def getHSEScore(loc, grid):
    column = [4, 10, 16, 22] #A, B, C, D
    row = [2, 4, 6, 8]
    c = loc[0]
    r = loc[1]

    adjLocs = [] # location adjacent to House
    indexRow = row.index(r) # check left and right
    if indexRow + 1 < 4: # check right
        build = grid[row[indexRow + 1]][c - 1] + grid[row[indexRow + 1]][c] + grid[row[indexRow + 1]][c + 1]
        adjLocs.append(build)
    if indexRow - 1 > -1: # check left
        build = grid[row[indexRow - 1]][c - 1] + grid[row[indexRow - 1]][c] + grid[row[indexRow - 1]][c + 1]
        adjLocs.append(build)

    indexCol = column.index(c)
    if indexCol + 1 < 4: # check up
        build = grid[r][column[indexCol + 1] - 1] + grid[r][column[indexCol + 1]] + grid[r][column[indexCol + 1] + 1]
        adjLocs.append(build)
    if indexCol - 1 > -1: # check down
        build = grid[r][column[indexCol - 1] - 1] + grid[r][column[indexCol - 1]] + grid[r][column[indexCol - 1] + 1]
        adjLocs.append(build)

    count = 0
    for loc in adjLocs:
        if loc == "   ":
            count += 0
        elif loc == "FAC":
            count == 1
            break
        else:
            if loc == "HSE" or loc == "SHP":
                count += 1
            elif loc == "BCH":
                count += 2

    return count

def getHWYArray(locArray):
    rArray = []
    hwyArray = []
    for i in locArray:
        locr = i[1]
        rArray.append(locr)
    for r in rArray:
        repeatCount = rArray.count(r)
        hwyArray.append(repeatCount)
    return hwyArray

def getHWYTotalScore(hwyArray):
    count = 0
    for i in hwyArray:
        count = count + i
    return count

def getShpScore(loc, grid):
    column = [4, 10, 16, 22] #A, B, C, D
    row = [2, 4, 6, 8]
    c = loc[0]
    r = loc[1]

    adjLocs = [] # locations that are adjacent to Shops

    indexRow = row.index(r) # check left and right
    if indexRow + 1 < 4: # check right
        build = grid[row[indexRow + 1]][c - 1] + grid[row[indexRow + 1]][c] + grid[row[indexRow + 1]][c + 1]
        adjLocs.append(build)
    if indexRow - 1 > -1: # check left
        build = grid[row[indexRow - 1]][c - 1] + grid[row[indexRow - 1]][c] + grid[row[indexRow - 1]][c + 1]
        adjLocs.append(build)

    indexCol = column.index(c)
    if indexCol + 1 < 4: # check up
        build = grid[r][column[indexCol + 1] - 1] + grid[r][column[indexCol + 1]] + grid[r][column[indexCol + 1] + 1]
        adjLocs.append(build)
    if indexCol - 1 > -1: # check down
        build = grid[r][column[indexCol - 1] - 1] + grid[r][column[indexCol - 1]] + grid[r][column[indexCol - 1] + 1]
        adjLocs.append(build)

    if "SHP" in adjLocs:
        adjLocs.remove("SHP")

    adjLocs = set(adjLocs)

    count = 0
    if(len(adjLocs) > 1):
        for l in adjLocs:
            count += 1
    else:
        count = 1
    return count

def locationEmpty():
    return 0

#Printing buildings score
#HSE: 1 + 5 + 6 + 4 = 16
#FAC: 1 = 1
#SHP: 1 + 1 + 3 = 5
#HWY: 3 + 3 + 3 = 9
#BCH: 3 + 3 + 3 + 1 = 10

def printBScore(scoreArray, type):
    if(type == "HSE"):
        totalscore = 0
        for i in scoreArray:
            totalscore = totalscore + i
        printstring = "HSE: " 
        if(len(scoreArray) == 1):
            if(scoreArray[0] == 0):
                printstring = "HSE: 0"
            else:
                scstr = str(scoreArray[0])
                printstring = "HSE: " + scstr + " = " + scstr
        else:
            count = 0
            for i in scoreArray:
                count +=1
                ind = scoreArray.index(i)
                if (count) == len(scoreArray):
                    printstring = printstring + str(scoreArray[ind]) + " = " + str(totalscore)
                else:
                    printstring = printstring + str(scoreArray[ind]) + " + "
            
        return print(printstring)

    if(type == "FAC"):
        total = getFACTotalScore(scoreArray)
        printstring = "FAC: " 
        if(len(scoreArray) == 1):
            if(scoreArray[0] == 0):
                printstring = "FAC: 0"
            else:
                scstr = str(scoreArray[0])
                printstring = "FAC: " + scstr + " = " + scstr 
        else:
            count = 0
            for i in scoreArray:
                count += 1
                ind = scoreArray.index(i)
                if (count) == len(scoreArray):
                    printstring = printstring + str(scoreArray[ind]) + " = " + str(total)
                else:
                    printstring = printstring + str(scoreArray[ind]) + " + "
            
        return print(printstring)

    if(type == "SHP"):
        totalscore = 0
        for i in scoreArray:
            totalscore = totalscore + i
        printstring = "SHP: " 
        if(len(scoreArray) == 1):
            if(scoreArray[0] == 0):
                printstring = "SHP: 0"
            else:
                scstr = str(scoreArray[0])
                printstring = "SHP: " + scstr + " = " + scstr
        else:
            count = 0
            for i in scoreArray:
                count +=1
                ind = scoreArray.index(i)
                if (count) == len(scoreArray):
                    printstring = printstring + str(scoreArray[ind]) + " = " + str(totalscore)
                else:
                    printstring = printstring + str(scoreArray[ind]) + " + "
            
        return print(printstring)

    if(type == "HWY"):
        total = getHWYTotalScore(scoreArray)
        printstring = "HWY: " 
        if(len(scoreArray) == 1):
            if(scoreArray[0] == 0):
                printstring = "HWY: 0"
            else:
                scstr = str(scoreArray[0])
                printstring = "HWY: " + scstr + " = " + scstr  
        else:
            count = 0
            for i in scoreArray:
                count +=1
                ind = scoreArray.index(i)
                if (count) == len(scoreArray):
                    printstring = printstring + str(scoreArray[ind]) + " = " + str(total)
                else:
                    printstring = printstring + str(scoreArray[ind]) + " + "
            
        return print(printstring)

    if(type == "BCH"):
        totalscore = 0
        for i in scoreArray:
            totalscore = totalscore + i
        printstring = "BCH: " 
        if(len(scoreArray) == 1):
            if(scoreArray[0] == 0):
                printstring = "BCH: 0"
            else:
                scstr = str(scoreArray[0])
                printstring = "BCH: " + scstr + " = " + scstr 
        else:
            count = 0
            for i in scoreArray:
                count +=1
                ind = scoreArray.index(i)
                if (count) == len(scoreArray):
                    printstring = printstring + str(scoreArray[ind]) + " = " + str(totalscore)
                else:
                    printstring = printstring + str(scoreArray[ind]) + " + "
            
        return print(printstring)

#Total score: 41
def printTotalScore(scoreArray):
    t = 0
    for i in scoreArray:
        t = t + i
    tstr = str(t)
    printstr = "Total score: " + tstr
    return print(printstr)