import pytest
from US7 import *


@pytest.mark.parametrize("cfm, expectedResult",
[("Y", False), ("N", False),("s",True)])

def test_buildingConfirm_breakReturn(cfm, expectedResult):
    result = buildingConfirm(cfm)
    assert result == expectedResult

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
