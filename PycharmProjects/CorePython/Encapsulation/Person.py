class Person:
    AVG_AGE = 18
    count = 0
    def __init__(self):
        self.__name = None
        self.__dob= None
        self.__address = None
        Person.count += 1
    def getname(self):
        return self.__name

    def getdob(self):
        return self.__dob

    def getaddress(self):
        return self.__address

    def setname(self,name):
        self.__name = name
    def setdob(self,dob):
        self.__dob = dob

    def setaddress(self,address):
        self.__address = address

person = Person()
person.setname("Ram")
person.setdob("28/March/2026")
person.setaddress("123 Main Street")
person.getname()
person.getdob()
person.getaddress()
print("Name of Person is",person.getname())
print("DOB of Person is",person.getdob())
print("Address of Person is",person.getaddress())
person2 = Person()
person2.setname("Shyam")
person2.setdob("28/March/1990")
person2.setaddress("ABC Street")
person2.getname()
person2.getdob()
person2.getaddress()
print("Name of Person is",person2.getname())
print("DOB of Person is",person2.getdob())
print("Address of Person is",person2.getaddress())
print(Person.count)