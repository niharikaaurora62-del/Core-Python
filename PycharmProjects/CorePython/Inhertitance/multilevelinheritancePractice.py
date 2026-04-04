class Person:
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")
        self.address = input("Address: ")

class StudyDetails(Person):
    def getStudyDetails(self):
        self.qualification = input("Qualification: ")
        self.qualificationpassingyear = int(input("Qualification passing year: "))
        self.qualificationpercentile = float(input("Qualification percentile: "))

class IsPersonElligible(StudyDetails):
    def iselligible(self):
        print("\n\nName:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Address:", self.address)
        print("Qualification:", self.qualification)
        print("Qualification passing year:", self.qualificationpassingyear)
        print("Qualification percentile:", self.qualificationpercentile)
        if self.qualification == "MBA":
            if self.qualificationpercentile > 8.5:
                print("The Person", self.name, "is elligible for this job" )
            else:
                print("The Person", self.name, "is NOT elligible for this job")
        else:
            print("The Person", self.name, "qualification not match with our requirements")


m = IsPersonElligible()
m.getStudent()
m.getStudyDetails()
m.iselligible()