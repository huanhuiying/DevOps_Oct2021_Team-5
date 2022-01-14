import pytest
from SimpCity import *
import re

#My objective is to find out if the location entered is inputted on the grid, hence when I enter a 
#location, i need to see my building name appear in my 4x4 grid
#Call the function from SimpCity.py


@pytest.mark.parametrize("location, expectedResult", 
[("a9", False), ("z1", False), ("a4", True), ("A4", True), ("A9", False), 
("Z1", False), ("z7", False), ("S7", False)])

def test_Building_To_Be_Printed(location, expectedResult):
    result = place_building(location, building_choice)
    assert result == expectedResult