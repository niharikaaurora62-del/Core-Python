try:
    from abc import ABC, abstractmethod


    class Person(ABC):
        def execute(self):
            self.persondetails()

        @abstractmethod
        def persondetails(self):
            pass


    class Details(Person):

        def persondetail(self):
            self.name = "Niharika Aurora"
            self.age = 20
            print("Name", self.name)
            print("Age", self.age)


    d1 = Details()
    d1.persondetail()
    # p1 = Person()
    # p1.persondetails()
except NotImplementedError as e:
    print("error is", e)