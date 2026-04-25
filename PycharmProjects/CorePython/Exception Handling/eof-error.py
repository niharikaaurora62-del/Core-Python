try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a+b
except EOFError as e:
    print(e)