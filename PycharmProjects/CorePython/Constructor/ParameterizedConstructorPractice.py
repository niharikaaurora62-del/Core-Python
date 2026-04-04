class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


s = Person("Niharika Aurora", 27)
print("Name: ", s.getName())
print("Age: ", s.getAge())

 # by Set Get Method
s.setName("Ram Shyam")
s.setAge(16)
print("Name: ", s.getName())
print("Age: ", s.getAge())