try:
    num = int(input("Enter a number: "))
    if num > 10:
        raise Exception("Invalid input")
except Exception as e:
    print("Error:",e)