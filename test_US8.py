#US8 - As a user, I want to be given a prompt to verify my decision 
# in placing a building so I do not accidentally place the building
#  in a position I do not want.

import pytest
from US8 import *

@pytest.mark.parametrize("cfm, expectedResult",
[("Y", False), ("N", False),("s",True)])

def test_positionConfirm_breakReturn(cfm, expectedResult):
    result = positionConfirm(cfm)
    assert result == expectedResult

def test_positionConfirm_y(capfd):
    positionConfirm("Y")

    out, er = capfd.readouterr()
    assert out == "Position confirmed\n"

def test_positionConfirm_n(capfd):
    positionConfirm("N")

    out, er = capfd.readouterr()
    assert out == "Cancelled\n"

def test_positionConfirm_others(capfd):
    positionConfirm("p")

    out, er = capfd.readouterr()
    assert out == "Use only 'Y' or 'N' to confirm\n"  

def test_positionConfirm_int(capfd):
    positionConfirm(9)

    out, er = capfd.readouterr()
    assert out == "Use only 'Y' or 'N' to confirm\n"  
