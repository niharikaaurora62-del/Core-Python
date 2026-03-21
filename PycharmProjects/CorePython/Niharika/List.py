#append
numbers = [1,2,4,5,6,7,8,9]
number1 = 56
numbers.append(number1)
print("After Append", numbers)

#count
numbers = [1,2,4,5,6,7,8,9,6,7,3,35,3,56,332,2,3]
number1 = numbers.count(6)
print("Total Count of 6 in list",number1)

#index
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
number1 = numbers.index(3)
print("Index of number 3 is",number1)

#insert
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
numbers.insert(3,77)
print("After Insert",numbers)

#Remove
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
numbers.remove(3)
print("After Remove",numbers)

#Reverse
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
numbers.reverse()
print("Reverse of numbers is",numbers)

#Sort
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
numbers.sort()
print("Sort of numbers is",numbers)

#Max
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
number1= max(numbers)
print("Max numbers is",number1)

#Min
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
number1= min(numbers)
print("Min numbers is",number1)

#tuple
numbers = [1,2,4,5,6,7,8,9,4,5,3,5,35,53,3]
list(numbers)
print("Tuple Convert",numbers)