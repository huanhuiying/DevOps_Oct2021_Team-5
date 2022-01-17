import pytest
from US6and12 import *

@pytest.mark.parametrize("location, expectedResult",
[("2", False), ("A2", True), ("b4", True), ("AA2", False), ("A6", False), ("F1", False)])

def test_LocationFormat_UserInput(location, expectedResult):
    result = location_format(location)
    assert result == expectedResult