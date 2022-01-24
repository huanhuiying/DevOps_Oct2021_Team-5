import pytest
from US22 import *

# US4 - As a user, I want to be able to select the "Exit"
#  option from the main menu so that I can end the program.

# US22 - As a user, I want to be shown a prompt to confirm my 
# choice to end the program so I don't accidentally end the program. 

def test_exitConfirm(cfm, expectedResult):
    result = exitConfirm(cfm)
    assert result == expectedResult

@pytest.mark.parametrize("cfm, expectedResult",
[("Y", False), ("N", False),("s",True)])

def test_exitConfirm_y(capfd):
    result = exitConfirm("Y")

    out, er = capfd.readouterr()
    assert out == "Exit confirmed.\nExiting application..."
    assert result == False

def test_exitConfirm_n(capfd):
    result = exitConfirm("N")

    out, er = capfd.readouterr()
    assert out == "Exit cancelled.\n"
    assert result == False

def test_exitConfirm_others(capfd):
    result = exitConfirm("l")

    out, er = capfd.readouterr()
    assert out == "Use only 'Y' or 'N' to confirm.\n"
    assert result == True


def test_exitConfirm_int(capfd):
    result = exitConfirm(3)

    out, er = capfd.readouterr()
    assert out == "Use only 'Y' or 'N' to confirm.\n"
    assert result == True




