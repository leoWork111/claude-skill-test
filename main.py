from utils import multiply, divide, greet

def hello():
    """Say hello to the world."""
    print("Hello, World!")

def add(a, b):
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    hello()
    print(f"1 + 2 = {add(1, 2)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(greet("Claude"))