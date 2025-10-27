# greetings.py
# Simple custom module providing greeting functions

def greet(name):
    """Return a simple greeting string."""
    return f"Hello, {name}!"

def polite_greet(name, title="Mr./Ms."):
    """Return a more polite greeting with a title."""
    return f"Hello, {title} {name}!"

# Module test code (runs only when you run this file directly)
if __name__ == "__main__":
    # This will run only when you run `python greetings.py`
    print(greet("Alice"))
    print(polite_greet("Alice", "Dr."))
