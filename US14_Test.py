import pytest
from US14 import *


@pytest.mark.parametrize("selected_buidling, no_buildings, expectedResult",
[("BCH",'{"BCH": 8, "FAC": 8, "HSE": 8, "SHP": 8, "HWY": 8}', True)])

def test_DeductBuildingChosen_UserInput(selected_buidling, no_buildings, expectedResult):
    result = deduct_building_chosen(selected_buidling, no_buildings)
    assert result == expectedResult