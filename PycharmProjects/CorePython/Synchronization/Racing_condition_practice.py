from time import sleep
from threading import *
import threading
from tkinter.font import names

class Employee:

    def __init__(self):
        self.salary = 0

    def set_salary(self, salary):
        sleep(1)
        self.salary = salary

    def get_salary(self):
        sleep(1)
        return self.salary

    def credit_salary(self, amount):
        sal = self.get_salary()
        self.set_salary(sal + amount)

class Racing(Thread):
    def __init__(self, account: Employee, name):
        super().__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.credit_salary(10000)
            print(self.name, self.account.get_salary())

def main_task():
    emp = Employee()
    t1 = Racing(emp, 'Shyam')
    t2 = Racing(emp, 'Ram')
    t1.start()
    t2.start()


main_task()