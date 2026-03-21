numbers = [10, 25, 3, 67, 40]

largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    elif num < largest:
        secondlargest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Second Largest number:", secondlargest)