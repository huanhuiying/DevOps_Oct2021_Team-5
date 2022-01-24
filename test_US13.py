import pytest
from US13 import *

# US13 - As a user, I would like to only be able to enter a number
#  for choices so that I do not get confused.


@pytest.mark.parametrize("choosen_configureMenu_option, expectedResult",
[(1, False), (3, False),(6, True)])


def test_configMenuVal(choosen_configureMenu_option, expectedResult):
    result = configMenuVal(choosen_configureMenu_option)
    assert result == expectedResult
   



