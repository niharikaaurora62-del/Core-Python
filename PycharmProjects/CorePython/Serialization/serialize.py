import pickle
class Employee:
    def __init__(self, eno,ename):
        self.eno = eno
        self.ename = ename
e = Employee(1, "Niharika")
f= open("C:/Users/LENOVO/Desktop/employee.txt","wb")
pickle.dump(e,f)
f.close()

