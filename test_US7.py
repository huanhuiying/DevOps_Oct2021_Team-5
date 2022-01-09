import pytest
from US7 import *

# @pytest.mark.parametrize("input, expectedResult",
# [("Y", "Building used."),("N", "Cancelled."),("p","Only use Y or N")])

def test_buildingConfirm_y(capfd):
    buildingConfirm("Y")

    out, er = capfd.readouterr()
    assert out == "Building confirmed\n"

def test_buildingConfirm_n(capfd):
    buildingConfirm("N")

    out, er = capfd.readouterr()
    assert out == "Cancelled\n"

def test_buildingConfirm_others(capfd):
    buildingConfirm("k")

    out, er = capfd.readouterr()
    assert out == "Use only 'Y' or 'N' to confirm\n"  

def test_buildingConfirm_int(capfd):
    buildingConfirm(6)

    out, er = capfd.readouterr()
    assert out == "Use only 'Y' or 'N' to confirm\n"  
