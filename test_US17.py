import pytest
from us17exit import *


#US17 - US17 - As a user, I want to be able to leave 
# the main menu at any point during the 16 rounds. 

#Print prompt for confirmation if "0" Exit is chosen 
#Call US21 Print Main Menu function if input to prompt is "Y"
#If input to prompt is "N", delete prompt
#If input to prompt is invalid, print error message and request user to retry

def test_ExitChosen():
    result = printPrompt()
    assert result == "Please enter 'Y' to confirm exiting to main menu or 'N' to cancel: "