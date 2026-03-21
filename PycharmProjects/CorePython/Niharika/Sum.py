a = 100
b = 201
total_sum = 0
for i in range(a, b):
    if i % 7 == 0:
        print(i, "is divisible by 7")
        total_sum += i
print(total_sum, "is total of all numbers divided by 7")
