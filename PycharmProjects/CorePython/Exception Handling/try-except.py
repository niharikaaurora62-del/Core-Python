a = 4
b = 0
try:
    c=a/b
    print("C:",c)
except ZeroDivisionError as e:
    print("Exception:",e)
    print("Check dividend")