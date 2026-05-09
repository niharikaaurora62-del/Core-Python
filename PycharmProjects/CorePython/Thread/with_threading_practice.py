import threading
from threading import *

def employee():
    for i in range(1, 6):
        print('This is employee thread:', i)

def employeedetails():
    for i in range(1, 6):
        print('This is employee details thread:', i)

t1 = threading.Thread(target=employee)
t2 = threading.Thread(target=employeedetails)
t1.start()
t2.start()