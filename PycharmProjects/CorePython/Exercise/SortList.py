list = [100,10,15,17,13,5]
print("List Before Sort",list)
list.reverse()
print("Ascending Order List",list)
list.sort(reverse=True)
print("Descending Order List",list)


tuple = (100,10,15,17,13,5)
print("Tuple before sort",tuple)
asctuple = sorted(tuple)
print("Ascending Order Tuple",asctuple)
dsctuple = sorted(tuple,reverse=True)
print("Descending Order Tuple",dsctuple)