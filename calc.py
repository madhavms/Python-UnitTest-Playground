def add(x,y):
    """Add Function"""
    return x + y

def subtract(x,y):
    """Subtract Function"""
    return x - y

def multiply(x,y):
    """Multiply Function"""
    return x * y

def divide(x,y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Cannot divide an integer by zero.')
    return x / y
