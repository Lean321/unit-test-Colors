import pytest
from colors import fcolor

@pytest.mark.parametrize("input,expect", [('quit','bye'),('blue','blue'),('black','Not a valid color')])
def test_fcolor(input,expect):
    output = fcolor(input)
    assert  expect == output
