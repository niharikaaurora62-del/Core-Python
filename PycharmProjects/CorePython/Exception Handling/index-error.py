list = [1,4,5,4]

try:
    print(list[4])
except IndexError as e:
    print("Index Error", e)