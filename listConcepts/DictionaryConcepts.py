
#Dictionary :
#Dictionary is a collection of key-value pairs.
# Dictionary is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
# Allows one None Key and Multiple None Values
# Allows Duplicate Values not duplicate keys

#Syntax:
#dict1={key1:value1,key2:value2,key3:value3}

dict1={"Name":"Rahul","Age":30,"City":"Bangalore"}

print(dict1)

#Size of the dictionary --> no of entries in the dictionary
print(len(dict1))

#Accessing the value using the key
print(dict1["Name"]) #Name
print(dict1["Age"]) #Age

#Accessing the value using the get() method
print(dict1.get("City")) #City

#Prints the list of values in the dictionary
print(dict1.values())

#Prints the list of keys in the dictionary
print(dict1.keys())

#Prints the list of key-value pairs in the dictionary
print(dict1.items())

#Adding a new key-value pair to the dictionary
dict1["Country"]="India"
dict1["Continent"] = "Asia"

print(dict1)

#Updating the value of the key in the dictionary
dict1["Country"]="USA"
print(dict1)

#Updating the values in the dictionary
dict1.update({"Continent":"North America"})
print(dict1)

#Checks if the key is present in the dictionary
print(
dict1.__contains__("Name"))

#Deleting the values from the dictionary based on the key
dict1.__delitem__("Age")
print(dict1)

#Setting the default value for the key
dict1.setdefault("Department","IT")
print(dict1)

#Copying the values from the dictionary
dict2=dict1.copy()

print(dict2)

#Removes the key-value pair from the dictionary
dict2.pop("Department")

print(dict2)

#Removes the last key-value pair from the dictionary
dict2.popitem()

print(dict2)

#Reverse the map of the dictionary
#Not working
dict2.__reversed__()

print(dict2)

#Clears the data from the dictionary
dict1.clear()