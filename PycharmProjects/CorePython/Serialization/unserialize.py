import pickle
c = ["viaksh", "shivani", "mohit", "tina"]
fileobj = open("C:/Users/LENOVO/Desktop/employeeunpickle.txt", 'wb')
pickle.dump(c, fileobj)
fileobj.close()