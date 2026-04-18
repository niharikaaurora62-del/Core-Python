from abc import ABC, abstractmethod
@abstractmethod
class Shape (ABC):
    def __init__(self, c,b):
        self.color = c
        self.borderwidth = b
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    PI = 3.14
    def area(self):
        return self.radius*self.radius*Circle.PI
c = Circle(2)
print(c.area())