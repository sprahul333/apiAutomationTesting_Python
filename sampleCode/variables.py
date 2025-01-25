a=40
b=50

print(a+b)

a="Hello"
b="World"

print(a+" "+b)

#Assigning multiple values to multiple variables
a,b,c=10,20,30

print(a+b+c)

#Assigning the same value to multiple variables
a=b=c=10

print("Value of a is",a)
print("Value of b is",b)
print("Value of c is",c)

#In Python we cannot concatenate a string with a number
#Throws RunTimeError --> TypeError: can only concatenate str (not "int") to str
# print("Value of a is "+a)

#Right Way to concatenate a string with a number
#str() function is used to convert the number to a string
print("Value of a is "+str(a))

#Data Types:
#Python has 4 inbuilt data types:
#1. Numberic
#2. String
#3. boolean
#4. None
#5. List
#6. Tuple


#For Numbers we have 3 types:
#1. int
#2. float
#3. complex
#4. long (deprecated in Python 3)

#Formatting the output
#Using the format() method

#The format() method formats the specified value(s) and insert them inside the string's placeholder.
#The placeholder is defined using curly brackets: {}
#The format() method returns the formatted string.

#Print Formatting
print(f'Value of c is {c}')

#Using the format() method
print("Value of c is {}".format(c))

#Using the format() method with multiple values
print("Value of a is {} and value of b is {}".format(a,b))

#Using the format() method with multiple values and placeholders
print("Value of a is {0} and value of b is {1}".format(a,b))