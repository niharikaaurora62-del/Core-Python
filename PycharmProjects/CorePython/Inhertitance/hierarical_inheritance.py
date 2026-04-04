class Shape:
    def __init__(self):
        self.color = ''
        self.borderWidth = 0

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, bw):
        self.borderWidth = bw

    def getBorderWidth(self):
        return self.borderWidth


class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def setLength(self, l):
        self.length = l

    def getLength(self):
        return self.length

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width

class Circle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def setLength(self, l):
        self.length = l

    def getLength(self):
        return self.length

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width

r = Rectangle()
r.setLength(10)
r.setWidth(20)
r.setColor("red")
r.setBorderWidth(100)

c = Circle()
c.setLength(20)
c.setWidth(30)
c.setColor("blue")
c.setBorderWidth(200)

print("Length of Rectangle:", r.getLength())
print("Width of Rectangle:", r.getWidth())
print("Color of Rectangle:", r.getColor())
print("Border Width of Rectangle:", r.getBorderWidth())
print("")
print("Length of Circle:", c.getLength())
print("Width of Circle:", c.getWidth())
print("Color of Circle:", c.getColor())
print("Border Width of Circle:", c.getBorderWidth())