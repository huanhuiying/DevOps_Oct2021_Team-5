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

@pytest.mark.parametrize("main_option, expectedResult",
[(1, False),(2, False),(0, False),(4,True),('a',True),('gsdf',True),(9,True)])

def test_mainMenuVal_breakReturn(main_option, expectedResult):
    result = mainMenuVal(main_option)
    assert result == expectedResult

def test_mainMenuVal_invalid(capfd):
    mainMenuVal(7)

    out, er = capfd.readouterr()
    assert out == "Please choose valid options.\n"

def test_mainMenuVal_string(capfd):
    mainMenuVal("gdf")

    out, er = capfd.readouterr()
    assert out =="Please choose valid options.\n"