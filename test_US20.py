import pytest
from exit import *

#Test script for US20
#Print prompt for confirmation if "0" Exit is chosen 
#Call US21 Print Main Menu function if input to prompt is "Y"
#If input to prompt is "N", delete prompt
#If input to prompt is invalid, print error message and request user to retry

def test_ExitChosen():
    result = printPrompt()
    assert result == "Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: "

def test_ExitPrompt_NoInput():
    result = exitToMenu()
    assert result == "Invalid input. Please enter 'Y' or 'N' to continue: "


@pytest.mark.parametrize("input, expectedresult", 
[("Y", printMenu()), ("N", "Exit to main menu is cancelled.")])

def test_Exit_UserInput(input, expectedresult):
    result = checkUserInput(input)
    assert result == expectedresult
