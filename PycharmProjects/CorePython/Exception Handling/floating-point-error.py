a = 11.7
b = 0.0

try:
    c = a / b
    print(c)
except FloatingPointError as e:
    print(e)