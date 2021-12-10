import pytest
from exit import *

#Test script for US20
#Print prompt for confirmation if "0" Exit is chosen 
#Call US21 Print Main Menu function if input to prompt is "Y"
#If input to prompt is "N", delete prompt
#If input to prompt is invalid, print error message and request user to retry


@pytest.mark.parametrize("flag, count, input, expectedresult", 
[(True, 0, "", print("Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")),
(True, 1, "Invalid", print("Invalid input. Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")),
 (False, 1, "Y", checkUserInput(input="Y")), (False, 1, "N", checkUserInput(input="N"))])

#first test
def test_ExitChosen(flag, count, input, expectedresult):
    result = printPrompt(flag, count, input)
    assert result == expectedresult

#@pytest.mark.parametrize("input, count, expectedresult", 
#[("Y", 0, printPrompt(bool=False, count=1, input="Y")), ("N", 0, printPrompt(bool=False, count=1, input="N")),
# ("Invalid", 0, printPrompt(bool=True, count=1, input="Invalid"))])

@pytest.mark.parametrize("input, count, resbool, rescount", 
[("Y", 0, False, 1), ("N", 0, False, 1),
 ("Invalid", 0, True, 1)])

def test_ExitPrompt_InvalidInput(input, count, resbool, rescount):
    result = validateUserInput(input, count)
    assert result == (resbool, rescount)


@pytest.mark.parametrize("input, expectedresult", 
[("Y", printMenu()), ("N", print("Exit to main menu is cancelled."))])

def test_Exit_UserInput(input, expectedresult):
    result = checkUserInput(input)
    assert result == expectedresult