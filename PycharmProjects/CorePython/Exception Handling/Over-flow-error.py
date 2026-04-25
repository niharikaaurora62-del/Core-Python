import math

try:
    # Raising e to the power of 1000 exceeds standard float limits
    result = math.exp(1000)
    print("Result:", result)
except OverflowError as e:
    # This block executes when the number is too high
    print(f"Error caught: {e}")
    print("The calculated number is too large to be represented.")
