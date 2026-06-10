"""
shipfast-api · Python App
Pipeline module — chains calculator functions together.
Used for integration testing demos.
"""

from calculator import add, subtract, multiply, divide, is_even


def calculate_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    discount = divide(multiply(price, discount_percent), 100)
    return subtract(price, discount)


def calculate_total(items):
    """Sum a list of item prices."""
    total = 0
    for price in items:
        total = add(total, price)
    return total


def calculate_average(items):
    """Calculate the average of a list of numbers."""
    total = calculate_total(items)
    return divide(total, len(items))


def is_bulk_order(quantity, threshold=10):
    """Return True if quantity qualifies as a bulk order."""
    return quantity >= threshold