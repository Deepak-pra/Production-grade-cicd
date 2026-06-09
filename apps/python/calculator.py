"""
shipfast-api · Python App
Simple calculator module used for CI/CD training demos.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a multiplied by b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0
