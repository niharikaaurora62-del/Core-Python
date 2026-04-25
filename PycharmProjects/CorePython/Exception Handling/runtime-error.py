numbers = {1, 2, 3}

try:
    # This loop tries to remove items from the set while looping through it
    for item in numbers:
        numbers.remove(item)
except RuntimeError as e:
    print("Caught a pre-built Runtime error:", e)