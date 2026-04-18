class shape:
    def __init__(self,c,b):
        self.color=c
        self.border_width=b
    def area(self):
        return -1
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_border_width(self,border_width):
        self.border_width=border_width
    def get_border_width(self):
        return self.border_width
class Circle(shape):
    PI = 3.14
    def __init__(self,r,c="",b=0):
        self.radius=r
        super(Circle,self).__init__(c,b)
    def area(self):
        print("Color is", self.color)
        return self.radius*self.radius*Circle.PI
c1 = Circle(2,"red", 5)
c2 = Circle(4,"blue")
c3 = Circle(5)
print("Circle Area")
print(c1.area())
print(c2.area())
print(c3.area())

class Rectangle(shape):
    def __init__(self,length,width,c="",b=0):
        self.length=length
        self.width=width
        super(Rectangle,self).__init__(c,b)
    def area(self):
        print("Color is", self.color)
        return self.length*self.width
r1 = Rectangle(2,3,"red",7)
r2 = Rectangle(4,5,"blue")
r3 = Rectangle(5,6)
print("Rectangle Area")
print(r1.area())
print(r2.area())
print(r3.area())

class Triangle(shape):
    def __init__(self,base,height,c="",b=0):
        self.base=base
        self.height=height
        super(Triangle,self).__init__(c,b)

    def area(self):
        print("Color is", self.color)
        return (self.base*self.height)/2

t1 = Triangle(2,3,"red",7)
t2 = Triangle(4,5,"blue")
t3 = Triangle(5,6)
print("Triangle Area")
print(t1.area())
print(t2.area())
print(t3.area())