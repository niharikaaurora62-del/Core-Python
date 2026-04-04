class Person:
    def __init__(self, name, age):
        print("Person Constructor Called")
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


class Details(Person):

    def __init__(self, qualification="", percentage=0.0, experience=0, name="", age=0):
        self.qualification = qualification
        self.percentage = percentage
        self.experience = experience
        super().__init__(name, age)

    def setQualification(self, qualification):
        self.qualification = qualification

    def getQualification(self):
        return self.qualification

    def setPercentage(self, percentage):
        self.percentage = percentage

    def getPercentage(self):
        return self.percentage
    def setExperience(self, experience):
        self.experience = experience
    def getExperience(self):
        return self.experience


d = Details("MBA (Business Analytics)", 89, 4, "Niharika Aurora", 26)
print("Details:")
print("Name:", d.getName())
print("Age:",d.getAge())
print("Qualification:", d.getQualification())
print("Percentage:", d.getPercentage())
print("Experience:", d.getExperience())