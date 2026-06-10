"""
Integration tests for pipeline.py
Tests how calculator functions work together through the pipeline module.
Run with: pytest tests/ -v
"""
import pytest
from pipeline import calculate_discount, calculate_total, calculate_average, is_bulk_order


class TestCalculateDiscount:
    def test_ten_percent_discount(self):
        assert calculate_discount(100, 10) == 90.0

    def test_fifty_percent_discount(self):
        assert calculate_discount(200, 50) == 100.0

    def test_zero_discount(self):
        assert calculate_discount(150, 0) == 150.0

    def test_discount_on_decimal_price(self):
        assert calculate_discount(99.99, 10) == pytest.approx(89.991, rel=1e-3)

    def test_full_discount(self):
        assert calculate_discount(100, 100) == 0.0


class TestCalculateTotal:
    def test_total_multiple_items(self):
        assert calculate_total([10, 20, 30]) == 60

    def test_total_single_item(self):
        assert calculate_total([99]) == 99

    def test_total_with_decimals(self):
        assert calculate_total([9.99, 4.99, 1.99]) == pytest.approx(16.97, rel=1e-3)

    def test_total_empty_list(self):
        assert calculate_total([]) == 0


class TestCalculateAverage:
    def test_average_basic(self):
        assert calculate_average([10, 20, 30]) == 20.0

    def test_average_single_item(self):
        assert calculate_average([42]) == 42.0

    def test_average_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculate_average([])


class TestIsBulkOrder:
    def test_bulk_order_above_threshold(self):
        assert is_bulk_order(15) is True

    def test_not_bulk_below_threshold(self):
        assert is_bulk_order(5) is False

    def test_exact_threshold(self):
        assert is_bulk_order(10) is True