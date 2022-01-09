import pytest
from US7 import *

def test_buildingConfirm():
    result = printBuildingCfm()
    assert result == "Y" or "N"

# def test_buildingConfirm_NoInput():
#     result = opt1()
#     assert result == "Invalid input. Confirm using building [Y/N]: "

@pytest.mark.parametrize("input, expectedResult",
[("Y", "Building used"),("N", "Not used"),("p","Please enter only Y or N")])

def test_buildingConfirm_userInput(input, expectedResult):
    result = checkUserInput(input)
    assert result == expectedResult