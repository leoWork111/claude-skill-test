def hello():
    """Say hello to the world."""
    print("Hello, World!")

def add(a, b):
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    hello()
    print(f"1 + 2 = {add(1, 2)}")