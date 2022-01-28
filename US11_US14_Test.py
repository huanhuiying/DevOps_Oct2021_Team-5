import pytest
import ast
from US11_US14 import *

# US 11
@pytest.mark.parametrize("no_buildings, expectedResult",
[('{"BCH": 8, "FAC": 8, "HSE": 8, "SHP": 8, "HWY": 8}', "Building        Remaining")])

def test_ShowRemainingBuilding_UserInput(no_buildings, expectedResult):
    no_buildings = ast.literal_eval(no_buildings)
    result = show_remaining_building(no_buildings)
    assert result == expectedResult

# US 14
@pytest.mark.parametrize("selected_buidling, no_buildings, expectedResult",
[("BCH",'{"BCH": 8, "FAC": 8, "HSE": 8, "SHP": 8, "HWY": 8}', True)])

def test_DeductBuildingChosen_UserInput(selected_buidling, no_buildings, expectedResult):
    no_buildings = ast.literal_eval(no_buildings)
    result = deduct_building_chosen(selected_buidling, no_buildings)
    assert result == expectedResult
