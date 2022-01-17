import pytest
from US10 import *

grid = []

file = open("game_grid_init.csv", "r")
for line in file:
    line = line.strip('\n')
    grid.append(list(line))

@pytest.mark.parametrize("location, expectedResult",
[("B1", True), ("A2", True), ("c1", True), ("b3", True), ("D4", False), ("b2", False)])

def test_ValidateLocation_UserInput(location, expectedResult):
    result = validate_location(location, grid)
    assert result == expectedResult