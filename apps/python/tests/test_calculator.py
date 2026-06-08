"""
Tests for calculator.py
Run with: pytest tests/ -v
"""
import pytest
from calculator import add, subtract, multiply, divide, is_even


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_add_zero(self):
        assert add(10, 0) == 10


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(10, 3) == 7

    def test_subtract_negative(self):
        assert subtract(5, -2) == 7


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(99, 0) == 0


class TestDivide:
    def test_divide_positive(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestIsEven:
    def test_even_number(self):
        assert is_even(4) is True

    def test_odd_number(self):
        assert is_even(7) is False

    def test_zero_is_even(self):
        assert is_even(0) is True
