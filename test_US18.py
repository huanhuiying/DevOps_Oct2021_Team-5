#US18 - As a user, I want to confirm exiting the game so that I don’t accidentally lose the save file
import pytest
from us18confirmexit import *
from us17exit import *

#Okay
@pytest.mark.parametrize("bool, count, input, eresult", 
[(True, 0, "Invalid", print("Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")), 
(True, 1, "Invalid", print("Invalid input. Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: ")),
(False, 1, "Y", checkUserInput("Y", 1)),
 (False, 1, "N", checkUserInput("N", 1))])

#Okay
def test_ExitChosen(bool, count, input, eresult):
    result = printExitPrompt(bool, count, input)
    assert result == eresult

#Okay
@pytest.mark.parametrize("i, c, rinput, rcount", 
[("Y", 0, False, 1),("N", 0, False, 1), ("Invalid", 0, True, 1)])

#Okay
def test_ExitPrompt_InvalidInput(i, c, rinput, rcount):
    result = checkUserInput(i, c)
    assert result == (rinput, rcount)

#Okay
@pytest.mark.parametrize("input, expectedresult", 
[("Y", True),
 ("N", False)])

#Okay
def test_Exit_ValidInput(input, expectedresult):
    result = checkValidInput(input)
    assert result == expectedresult

#Okay

@pytest.mark.parametrize("saveb, savec, savei, saveresult", 
[(True, 0, "Invalid", print("Please enter 'Y' to save before exiting and 'N' to exit without saving. Please note that any unsaved data will be lost: ")), 
(True, 1, "Invalid", print("Invalid input. Please enter 'Y' to save before exiting and 'N' to exit without saving. Please note that any unsaved data will be lost: ")),
(False, 1, "Y", checkSaveInput("Y", 1)),
 (False, 1, "N", checkSaveInput("N", 1))])

#Okay
def test_SaveChosen(saveb, savec, savei, saveresult):
    result = printSavePrompt(saveb, savec, savei)
    assert result == saveresult


#Okay
@pytest.mark.parametrize("si, sc, sinput, scount", 
[("Y", 0, False, 1),("N", 0, False, 1), ("Invalid", 0, True, 1)])

#Okay
def test_SavePrompt_InvalidInput(si, sc, sinput, scount):
    result = checkSaveInput(si, sc)
    assert result == (sinput, scount)


#Okay
@pytest.mark.parametrize("saveinput, saveexpectedresult", 
[("Y", exitToMainMenu()), ("N", exitToMainMenu())])


#Okay
def test_Save_ValidInput(saveinput, saveexpectedresult):
    result = checkValidSaveInput(saveinput)
    assert result == saveexpectedresult