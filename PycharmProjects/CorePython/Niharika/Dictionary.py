dictionary  = {'firstname':'Niharika','lastname':'Aurora', 'age': 26}
print(dictionary)
print("First Name" ,dictionary['firstname'])
print("Last Name" , dictionary['lastname'])
print("Age" , dictionary['age'])
print("length" , len(dictionary))
n = dictionary['firstname']
print("Extract First Name from key in variable" ,n)
keys = dictionary.keys()
print("Keys :", keys)
values = dictionary.values()
print("Values :", values)
name = dictionary.get('firstname')
print("Extract Name", name)
dictionary2 = dictionary.copy()
print("Copy Dictionary" ,dictionary2)
named2 = dictionary2['firstname'] = "ABC"
print("Name update in copy Dictionary" ,dictionary2)
# dictionary.clear()
# print("Dictionary cleared", dictionary)
del dictionary['firstname']
print("Delete First Name from dictionary" ,dictionary)
print("length" , len(dictionary))
# del dictionary
# print("Delete dictionary")
