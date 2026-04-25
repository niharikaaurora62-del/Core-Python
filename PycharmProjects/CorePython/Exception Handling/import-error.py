try:
    from abc import ABD, abstractmethod
    class Person(ABC):
        def execute(self):
            self.persondetails()
        @abstractmethod
        def persondetails(self):
            pass
    class Details(Person):

        def persondetails(self):
            self.name = "Niharika Aurora"
            self.age = 20
            print("Name", self.name)
            print("Age", self.age)
    d1 = Details()
    d1.persondetails()
    # p1 = Person()
    # p1.persondetails()
except ImportError as e:
    print("error is" ,e)
