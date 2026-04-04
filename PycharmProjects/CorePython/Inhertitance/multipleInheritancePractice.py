class Person:
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")
        self.address = input("Address: ")

class School:
    def getSchoolDetails(self):
        self.school_name = input("School Name: ")
        self.classpercentange = int(input("10th class Percentage: "))
        self.highclasspercentange = int(input("12th class Percentage: "))
        self.passingyear = input("Passing Year: ")

class Check(Person, School):  # derived class inherits both addition and mu,tiplacation base class
    def iselligible(self):
        print("\n\nName:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Address:", self.address)
        print("School Name:", self.school_name)
        print("10th Class Percentage:", self.classpercentange)
        print("12th Class Percentage:", self.highclasspercentange)
        print("Passing Year:", self.passingyear)
        # if self.highclasspercentange > 85:
        #     if self.classpercentange > 95:
        #         print("The Person", self.name, "is elligible for the IIM Course")
        #     else:
        #         print("The Person", self.name, "is NOT elligible the IIM Course")
        # else:
        #     print("The Person", self.name, " is not elligible for any IIM, IIT Course")
        #

c1 = Check()
print(c1.getStudent())
print(c1.getSchoolDetails())
# print(c1.iselligible())