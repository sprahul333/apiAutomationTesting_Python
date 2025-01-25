#Inheritance --> Inheriting the properties of one class into another class
#Inheriting the methods, variables, objects into another class

class Car:

    maxSpeed=100

    def __init__(self):
        print("Car from Parent Class")


    def startEngine(self):
        print("Car Started")

    def stopEngine(self):
        print("Car Stopped")

class Audi(Car):

    def __init__(self):
        super().__init__() #Referring to the parent class constructor
        print("Audi from Child Class")

    def startEngine(self):
        print("Audi Started")


car=Audi()
car.startEngine()