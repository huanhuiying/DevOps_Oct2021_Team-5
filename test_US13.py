import pytest
from US13 import *

# US13 - As a user, I would like to only be able to enter a number
#  for choices so that I do not get confused.


@pytest.mark.parametrize("option, expectedResult",
[(1, False),(2, False),(3, False),(4, False),(5, False),
(7,True),(0, False)])

def test_configMenuVal_breakReturn(option, expectedResult):
    result = configMenuVal(option)
    assert result == expectedResult
   
def test_configMenuVal_invalid(capfd):
    configMenuVal(7)

    out, er = capfd.readouterr()
    assert out == "Please choose valid options.\n"

def test_configMenuVal_string(capfd):
    configMenuVal("g")

    out, er = capfd.readouterr()
    assert out =="Please choose valid options.\n"
