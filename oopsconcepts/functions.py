#Function -> Group of statements that help us in performing the specified tasks

def greet():
    print("Hello World")


greet()

#Function with Parameters
def greetWithName(name):
    print("Hello",name)

greetWithName("John")

#Function with Return Type and arguments
def sumofnumbers(a,b):
    return a+b

print(sumofnumbers(10,20))

#Function with Default Arguments
def greetWithName(name="John"):
    print("Hello",name)

greetWithName()

#Function with *args -> Variable Length Arguments
def greetWithName(*name):

    #*name is a Tuple
    #Iterating over the Tuple
    for names in name:
        print("Hello",names)

greetWithName("John","Doe","Smith")

#Function with ** kwargs -> Keyword Arguments

def printMessage(**name):
        #**name is a Dictionary
        #Iterating over the Dictionary
        for key,value in name.items():
            print("Message from",key,"is",value)

printMessage(John="Hello",Doe="Hi",Smith="Good Morning")