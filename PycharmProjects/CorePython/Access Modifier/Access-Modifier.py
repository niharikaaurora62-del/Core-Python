class Employee:
    def __init__(self):
        self.name = ""
        self._code = ""
        self.__salary = 0

    def getSalary(self):
        return self.__salary
    def setSalary(self, salary):
        self.__salary = salary
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def setCode(self, code):
        self._code = code
    def getCode(self):
        return self._code


class EmployeeDetails(Employee):
    def __init__(self):
        self.employeeaddress = ""

    def getEmployeeAddress(self):
        return self.employeeaddress
    def setEmployeeAddress(self, address):
        self.employeeaddress = address

print("EmployeeDetails")
ed = EmployeeDetails()
name = ed.setName("Ram Sharma")
code = ed.setCode("E101")
salary = ed.setSalary(25000)
address = ed.setEmployeeAddress("Indore")
print(ed.getEmployeeAddress())
print(ed.getSalary())
print(ed.getName())
print(ed.getCode())