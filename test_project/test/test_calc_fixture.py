import pytest
from src.calculator import(add, subtract, multiply, divide)

@pytest.fixture(scope="function")
def sample_data():
    return {
        "a": 5,
        "b": 3,
        "expected_sum": 8,
        "expected_difference": 2,
        "expected_product": 15,
        "expected_division": 5 / 3
    }

def test_add(sample_data):
    assert add(sample_data["a"], sample_data["b"]) == sample_data["expected_sum"]

def test_subtract(sample_data):
    assert subtract(sample_data["a"], sample_data["b"]) == sample_data["expected_difference"]

def test_multiply(sample_data):
    assert multiply(sample_data["a"], sample_data["b"]) == sample_data["expected_product"]

def test_divide(sample_data):
    assert divide(sample_data["a"], sample_data["b"]) == sample_data["expected_division"]

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1,0)