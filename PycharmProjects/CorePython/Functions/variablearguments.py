def sumNum(a, *varg):
    t = a
    for n in varg:
        t += n
    return t

total = sumNum(1,2,3,4,5,6,7,8,9,10)
print("Total is", total)

def multiplyNum(a, *varg):
    t = a
    for n in varg:
        t *= n
    return t
multiple = multiplyNum(1,2,3,4,5,6,7,8,9,10)
print("Multiply is", multiple)

def subtractNum(a, *varg):
    t = a
    for n in varg:
        t -= n
    return t
total = sumNum( 1,2,3,4,5,6,7,8,9,10)
print("Subtract is", subtractNum(100,total))

def divideNum(a, *varg):
    t = a
    for n in varg:
        t /= n
    return t
total = sumNum( 1,2,3,4,5,6,7,8,9,10)
print("Divide is", divideNum(100,total))