class Automobile:
    NO_OF_GEARS = 5

    def __init__(self):
        self.colour = None
        self.speed = None
        self.make = None
        self.model = None

    def getcolour(self):
        return self.colour

    def setcolour(self, colour):
        self.colour = colour

    def getspeed(self):
        return self.speed

    def setspeed(self, speed):
        self.speed = speed

    def getmake(self):
        return self.make

    def setmake(self, make):
        self.make = make

    def getmodel(self):
        return self.model

    def setmodel(self, model):
        self.model = model


automobile = Automobile()
automobile.setcolour("red")
automobile.setspeed(100)
automobile.setmake("TATA")
automobile.setmodel("Punch")
colour = automobile.getcolour()
speed = automobile.getspeed()
make = automobile.getmake()
model = automobile.getmodel()
gears = getattr(automobile, "NO_OF_GEARS")
print("We have a car of",make,"Company", "with colour",colour, ",has max speed of", speed, ",the model is", model, "and has",gears,"gears")
