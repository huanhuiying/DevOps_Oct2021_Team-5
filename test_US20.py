import pytest
from exit import *

#Test script for US20

@pytest.mark.parametrize("count, expectedresult", 
[(16, True), (5, False)])

def test_Game_Ended(count, expectedresult):
    result = exitAfterGameEnd(count)
    assert result == expectedresult
