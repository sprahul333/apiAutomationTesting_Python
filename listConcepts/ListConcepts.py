#Syntax of creating a list
#list1=[10,20,30,40,50,60]

#Features of List:
#1. List is a collection of items which allows multiple values
#2. List is ordered
#3. List is mutable and allows duplicate values
#4. List is represented by []
#5. Allows None values
list1=[30,40,50,60,80,100]

print(list1)

#Value at 1st Index Position
print(list1[1])

#Prints the values from 1st Index Position to 4th Index Position
#Inclusive of start index and exclusive of end index
print(list1[1:4])

#Prints the last Value in the list
print(list1[-1])

#Prints the second last value in the list
print(list1[-2])

#Inserting the value at the end of the list
list1.append(200)

#Inserting the value to the list at the 2nd Index Position
list1.insert(2,"Rahul")

print(list1)

#Update the value at the 3rd Index Position
list1[3]="Kumar"

print(list1)

#Remove the value from the list
list1.remove(200)

print(list1)

#Remove the value from the list at the 4th Index Position
value=list1.pop(4)

print(value)

print(list1)

#Prints the frequency of the value in the list
print(list1.count(30))

#Prints the size of the list
print(len(list1))

#Prints the index of the first occurence of the given value in the list
print(list1.index(30))

#Reverses the list
list1.reverse()

print(list1)

#Sorts the data in ascending order
#Applicable when the list has same type of values
# list1.sort()
#
# print(list1)

#Sorts the data in descending order
#Applicable when the list has same type of values
# list1.sort(reverse=True)
#
# print(list1)

#Copying the list
list2=list1.copy()

print(list2)

#Extend the list with multiple values
list2.extend([200,300,400])

print(list2)

#Find the index of the value in the list between 5th and 10th Index Position
print(list2.index(300,5,10))

#Sort the list from the 3rd Index Position
# list2.sort(3)

#Remove all the values from the list
list1.clear()


