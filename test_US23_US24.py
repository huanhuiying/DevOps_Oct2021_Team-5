import pytest
from US23_US24 import *

highscore_dict = {'Rachel': 52, 'Bob': 56, 'Alex': 34, 'Hello': 46, 'John': 48}
highscore_dict2 = {'Rachel': 52, 'Bob': 56, 'Alex': 34, 'Hello': 46, 'John': 48, 'Lisa': 58, 'Jessica': 38, 'Aaron': 33, 'Tom': 50, 'Thomas': 60, 'Fred': 57}

# US23
@pytest.mark.parametrize("highscore_dict, expectedResult",
[(highscore_dict, ['Bob', 'Rachel', 'John', 'Hello', 'Alex']),
(highscore_dict2, ['Thomas', 'Lisa', 'Fred', 'Bob', 'Rachel', 'Tom', 'John', 'Hello', 'Jessica', 'Alex'])])

def test_PrintLeaderboard_UserInput(highscore_dict, expectedResult):
    result = print_leaderboard(highscore_dict)
    assert result == expectedResult

# US24
@pytest.mark.parametrize("score, highscore_dict, expectedResult",
[(54, highscore_dict, 2), (30, highscore_dict, 6), (47, highscore_dict, 4)])

def test_CheckPosition_UserInput(score, highscore_dict, expectedResult):
    result = check_position(score, highscore_dict)
    assert result == expectedResult

@pytest.mark.parametrize("name, expectedResult",
[("Leonard", True), ("Jessica", True), ("Ihavemorethantwentychar", False)])

def test_CheckNameInput_UserInput(name, expectedResult):
    result = check_name_input(name)
    assert result == expectedResult

@pytest.mark.parametrize("name, score, highscore_dict, expectedResult",
[("Leonard", 36, highscore_dict, {'Rachel': 52, 'Bob': 56, 'Alex': 34, 'Hello': 46, 'John': 48, 'Leonard': 36}), 
("Jessica", 58, highscore_dict, {'Rachel': 52, 'Bob': 56, 'Alex': 34, 'Hello': 46, 'John': 48, 'Leonard': 36, 'Jessica': 58})])

def test_SaveScore_UserInput(name, score, highscore_dict, expectedResult):
    result = save_score(name, score, highscore_dict)
    assert result == expectedResult