def sum(a, b):
    c = a + b
    return c

print("Sum is",sum(5,10))

def mutltiply(a,b):
    c = a * b
    return c

print("Multiply is",mutltiply(5,15))

def divide(a,b):
    c = a / b
    return c

print("Division is",divide(75,15))

def subtract(a,b):
    c = a - b
    return c

print("Subtract is",subtract(75,15))


def sumdefault(a,b=12):
    c = a + b
    return c

print("Sum with default value is",sumdefault(16))