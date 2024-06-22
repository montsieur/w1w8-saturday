import pytest
from src.calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3), 
    (5, 6, 11), 
    (1, 1, 5)])

def test_add(a,b,expected):
    assert add (a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1), 
    (5, 6, -1), 
    (1, 1, 5)])

def test_subtract(a,b,expected):
    assert subtract (a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2), 
    (12, 6, 5), 
    (1, 1, 1)])

def test_divide(a,b,expected):
    assert divide (a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1,0)
