class Doctor:
    def __init__(self):
        self.name = ''
        self.age = 0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


class HeartSpecialist(Doctor):
    def __init__(self):
        self.specialization = ""

    def setSpecialization(self, specialization):
        self.specialization = specialization

    def getSpecialization(self):
        return self.specialization

class Ent(Doctor):
    def __init__(self):
        self.specialization = ""

    def setSpecialization(self, specialization):
        self.specialization = specialization

    def getSpecialization(self):
        return self.specialization

hs = HeartSpecialist()
hs.setSpecialization("Heart Specialist")
hs.setAge(26)
hs.setName("Niharika Aurora")

e = Ent()
e.setSpecialization("ENT Specialist")
e.setAge(24)
e.setName("Ram Shyam")

print("Name of Doctor:", hs.getName())
print("Age of Doctor:", hs.getAge())
print("Specialization of Doctor:", hs.getSpecialization())
print("")
print("Name of Doctor:", e.getName())
print("Age of Doctor:", e.getAge())
print("Specialization of Doctor:", e.getSpecialization())