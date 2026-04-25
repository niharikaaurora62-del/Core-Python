a = 20
b = 0

try:
    c = a/b
    print(c)
except ArithmeticError as e:
    print(e)