source = open("C:/Users/LENOVO/Desktop/Dog.jpeg","w")
target = ("C:/Users/LENOVO/Desktop/"
          ""
          ""
          "")

f1 = open(source, "rb")   # source image open
f2 = open(target, "wb")   # target file open

data = f1.read()          # source ki image read
f2.write(data)            # target me write

f1.close()
f2.close()

print("Image copied successfully!")