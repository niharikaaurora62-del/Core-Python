a = 10
b = 0
try:
    c = a/b
    print("C:",c)
except ZeroDivisionError as e:
    print("Error:",e)
finally:
    print("Finally:Always Execute")