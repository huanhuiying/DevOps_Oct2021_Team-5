#US15 - As a user, I want to be able to see my current score during each round to see 
# how much score I have accumulated to plan my next moves. (5)
import pytest
from US15andUS19 import *
#Create scores list for round (Don't Need Test)

#Create game scores list for all rounds (Don't Need Test)
#Need to check first of grid
#If building, check type (Need Test)
#First assign marks without any influence (Need Test)

#Then check for adjacent buildings (Need Test)
#Assign marks based on that (Need Test)
#calculate total mark for the building (Need Test)
# add to scores list (Don't Need Test)
#move onto next building
#once all buildings are done  
#calculate buildings total score (Need Test)
#add total score to game score list  (Don't Need Test)
#print out score (Need Test)

grid = []

file = open("game_grid_testus15_19.csv", "r")
for line in file:
    line = line.strip('\n')
    grid.append(list(line))

#column = [4, 10, 16, 22] #A, B, C, D
#row = [2, 4, 6, 8]

#a1 (Correct)
#a2 (Correct)
#c2 (Correct)
#b3 (Correct)
#c4 (Correct)
#d4 (Correct)
#b2 (Correct)

@pytest.mark.parametrize("location, expectedResult",
[([4, 2], "SHP"), ([4, 4], "BCH"), ([16, 4], "HSE"), ([10, 6], "SHP"), ([16, 8], "HWY"), ([22, 8], ""), ([10, 4], "HSE")])

#If building, check type (Need Test)
def test_TypeOfBuilding(location, expectedResult):
    result = findType(location, grid)
    assert result == expectedResult

#column = [4, 10, 16, 22] #A, B, C, D
#row = [2, 4, 6, 8]

#a2
#a3
#d2
#c3

#If Building is BCH
@pytest.mark.parametrize("location, expectedResult",
[([4, 4], 3), ([4, 6], 3), ([22, 4], 3), ([16, 6], 1)])

def test_getBCHScore(location, expectedResult):
    result = getBCHScore(location)
    assert result == expectedResult

#If Building is FAC
#There will be a FAC Count 
#Once A Building is Found will added to a count
#so result will be the count

@pytest.mark.parametrize("facCount, facResult",
[(1, 1), (2, [2, 2]), (3, [3, 3, 3]), (4, [4, 4, 4, 4]), (5, [4, 4, 4, 4, 1])])

def test_getFACScoreArray(facCount, facResult):
    result = getFACScoreArray(facCount)
    assert result == facResult

#Calculate Total Score of FAC
@pytest.mark.parametrize("facArray, facResult",
[([2, 2], 4), ([3, 3, 3], 9), ([4, 4, 4, 4], 16), ([4, 4, 4, 4, 1], 17)])

def test_getFACTotalScore(facArray, facResult):
    result = getFACTotalScore(facArray)
    assert result == facResult

#If Building is HSE

#column = [4, 10, 16, 22] #A, B, C, D
#row = [2, 4, 6, 8]

#HSE: c1, b2, c2, d3

#Get HSE Score
@pytest.mark.parametrize("location, expectedResult",
[([16, 2], 1), ([10, 4], 5), ([16, 4], 6), ([22, 6], 4)])

def test_getHSEScore(location, expectedResult):
    result = getHSEScore(location, grid) #added grid
    assert result == expectedResult

#If Building is HWY

#["a4", "b4", "c4", "d4"]
#["a1", "b1", "a2", "b3", "c4"]

#column = [4, 10, 16, 22] #A, B, C, D
#row = [2, 4, 6, 8]

@pytest.mark.parametrize("locArray, hwyResult",
[([[4, 8], [10, 8], [16, 8], [22, 8]], [4, 4, 4, 4]), ([[4, 2], [10, 2], [4, 4], [10, 6], [16, 8]], [2, 2, 1, 1, 1])])

def test_getHWYArray(locArray, hwyResult):
    result = getHWYArray(locArray)
    assert result == hwyResult

#Calculate Total Score of HWY

@pytest.mark.parametrize("hwyArray, hwyResult",
[([4, 4, 4, 4], 16), ([2, 2, 1, 1, 1], 7)])

def test_getHWYTotalScore(hwyArray, hwyResult):
    result = getHWYTotalScore(hwyArray)
    assert result == hwyResult


#If Building is SHP
#column = [4, 10, 16, 22] #A, B, C, D
#row = [2, 4, 6, 8]

#SHP: a1, b1, b3

@pytest.mark.parametrize("loc, shpResult",
[([4, 2], 1), ([10, 2], 1), ([10, 6], 3)])

def test_getShpScore(loc, shpResult):
    result = getShpScore(loc, grid)
    assert result == shpResult

#If the Location is empty

def test_locationEmpty():
    result = locationEmpty()
    assert result == 0

#Printing buildings score
#HSE: 1 + 5 + 6 + 4 = 16
#FAC: 1 = 1
#SHP: 1 + 1 + 3 = 5
#HWY: 3 + 3 + 3 = 9
#BCH: 3 + 3 + 3 + 1 = 10

@pytest.mark.parametrize("scoreArray, type, scoreResult",
[([1, 5, 6, 4], "HSE", print("HSE: 1 + 5 + 6 + 4 = 16")), 
([1], "FAC", print("FAC: 1 = 1")), ([1, 1, 3], "SHP", print("SHP: 1 + 1 + 3 = 5")), 
([3, 3, 3], "HWY", print("HWY: 3 + 3 + 3 = 9")), 
([3, 3, 3, 1], "BCH", print("BCH: 3 + 3 + 3 + 1 = 10"))])

def test_printBScore(scoreArray, type, scoreResult):
    result = printBScore(scoreArray, type)
    assert result == scoreResult

#Total score: 41

@pytest.mark.parametrize("scoreArray, scoreResult",
[([16, 5, 9, 10], print("Total score: 41")), 
([12, 2, 4, 9], print("Total score: 27"))])

def test_printTotalScore(scoreArray, scoreResult):
    result = printTotalScore(scoreArray)
    assert result == scoreResult