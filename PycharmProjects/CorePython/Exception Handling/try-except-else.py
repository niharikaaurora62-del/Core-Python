a = 5
b = 2
try:
    c = a/b
    print("C:",c)
except ZeroDivisionError as e:
    print("Error:",e)
else:
    print("No error")