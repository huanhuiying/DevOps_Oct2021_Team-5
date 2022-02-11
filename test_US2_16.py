import pytest
from US2_16 import *

mapfile = "savecontent/savefile.csv"
buildingfile = "savecontent/buildingCount.csv"
turnfile = "savecontent/turncount.csv"

mapcontent = []
buildingcontent = []
countcontent = []

def load_file(content,filename):
    file = open(filename, "r")
    for line in file:
        line = line.strip('\n')
        content.append(list(line))
        
    return content

mapExpected = load_file(mapcontent,mapfile)
buildingExpected = load_file(buildingcontent,buildingfile)
turnExpect = load_file(countcontent,turnfile)

grid=[]
file = open(mapfile, "r")
for line in file:
    line = line.strip('\n')
    grid.append(list(line))

@pytest.mark.parametrize("filename, content, expectedResult",
[(mapfile, mapcontent, mapExpected), 
(buildingfile, buildingcontent, buildingExpected),
(turnfile, countcontent, turnExpect)])

def test_savegame(filename, content, expectedResult):
    result = load_file(content,filename)
    assert result == expectedResult



