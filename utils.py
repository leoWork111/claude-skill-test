"""Utility functions for common operations."""

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers. Raises error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"