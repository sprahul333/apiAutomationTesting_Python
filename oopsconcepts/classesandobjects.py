#Constructor is one method which gets automatically called when we create an object of a class
#No Need of new keyword while creating the object
class Calculator:

    num=100 #Class Variable as the variable is declared inside the class but outside the method

    #On Creating an Object, during the runtime a default constructor is called
    #Constructor is a special method in Python

    def __init__(self):
        print("I am a default constructor")

    def __init__(self, a, b):
        print("I am a parameterized constructor")

        #Instance Variables as the variable is declared inside the method and also attached to the object

        self.firstNumber=a #Attaching the variable firstNumber to the object
        self.secondNumber=b #Attaching the variable secondNumber to the object
        print("I am called automatically when the object is created")

    #self is the first argument to any method in a class in Python
    #self helps to access the attributes and methods of the class
    def add(self, a, b):
        return a + b #Here a and b are the parameters and also local variables

    def add(self):
        #Syntax for calling the class variable
        #ClassName.variableName
        return self.firstNumber+self.secondNumber+Calculator.num

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

#Creating an object of the class
#self is passed as an argument to the constructor to refer to the current object
c1=Calculator(10,20) #Syntax to create objects in java

print(c1.add())

# print(c1.add(10,20))
# print(c1.subtract(20,10))