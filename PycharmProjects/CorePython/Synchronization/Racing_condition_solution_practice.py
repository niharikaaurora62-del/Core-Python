from time import sleep
from threading import Thread, Lock


class Employee:

    def __init__(self):
        self.salary = 0
        self.lock = Lock()   # 🔒 Lock add kiya

    def set_salary(self, salary):
        sleep(1)
        self.salary = salary

    def get_salary(self):
        sleep(1)
        return self.salary

    def credit_salary(self, amount):
        with self.lock:   # 🔒 Yaha lock laga diya
            sal = self.get_salary()
            self.set_salary(sal + amount)

class Racing(Thread):

    def __init__(self, account, name):
        super().__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.credit_salary(10000)
            print(self.name, self.account.get_salary())

def main_task():
    acc = Employee()

    t1 = Racing(acc, 'abc')
    t2 = Racing(acc, 'xyz')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Salary:", acc.salary)


main_task()