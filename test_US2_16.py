import pytest
from US2_16 import *


mapfile = "savecontent/savefile.csv"
buildingfile = "savecontent/buildingCount.csv"
turnfile = "savecontent/turncount.csv"
content = []
def load_file(content,filename):
    file = open(filename, "r")
    for line in file:
        line = line.strip('\n')
        content.append(list(line))
        
    return content

mapExpected = load_file(content,mapfile)
buildingExpected = load_file(content,buildingfile)
turnExpect = load_file(content,turnfile)

grid=[]
file = open(mapfile, "r")
for line in file:
    line = line.strip('\n')
    grid.append(list(line))


@pytest.mark.parametrize("grid, expectedResult",
[(grid, mapExpected)])

def test_savegame(grid, expectedResult):
    result = save_game(grid)
    assert result == expectedResult

