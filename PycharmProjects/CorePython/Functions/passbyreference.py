def changelist(list):
    list.append(13)
    # print("Changed List",list)
    return list

list = [1,3,5,67,321,344]
print(list)
changelist(list)
print("Changed List",list)

def countlist(list):
    result = list.count(644)
    # print(result)
    return result

list = [23,55,66,74,644,35,13]
print(list)
result = countlist(list)
append = changelist(list)
print("count of 644 is", result)
print("Updated list is ", append)