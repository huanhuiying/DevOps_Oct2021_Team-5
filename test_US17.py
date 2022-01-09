import pytest
from us17exit import *

#US17 - US17 - As a user, I want to be able to leave 
# the main menu at any point during the 16 rounds. 

def test_ExitingToMainMenu():
    result = exitToMainMenu()
    assert result == print("Exiting To Main Menu")