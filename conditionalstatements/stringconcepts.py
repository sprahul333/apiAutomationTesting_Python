#strings is nothing but combination of characters

str1="Sample Data"

#Prints the length of the string
print(len(str1))

#Prints the string in capital letters
print(str1.upper())

#Prints the string in small letters
print(str1.lower())

#Prints the string in title case
print(str1.title())

#Replace the word in the string
print(str1.replace("Data","Information"))

#Prints the string in reverse order
print(str1[::-1])

#Prints the substring from 2nd Index Position to 5th Index Position
print(str1[2:5])

#Prints the substring from 2nd Index Position to 5th Index Position in reverse order
print(str1[5:2:-1])

#Prints the string starting from 3rd Index Position till the end
print(str1[3::])

#Checks if the word is present in the string
print(str1.__contains__("Data"))
print ("Data" in str1)

str1= "               Hello World                    "

#Removes the white spaces that is present at the start and at the end of the string
print(str1.strip())

#Removes the white spaces that is present at the start of the string
print(str1.lstrip())

#Removes the white spaces that is present at the end of the string
print(str1.rstrip())

#Checks if the string is starting with the given word
print(str1.startswith("Hello"))

#Checks if the given string is ending with the given word
print(str1.endswith("World"))

#Splits the string based on the given character
#Returns a list of strings
print(str1.strip().split(" "))

#Print the list of words
print("**************Printing the list of words***********************************")
for word in str1.strip().split(" "):
    print(word)

print("**************Printing the list of words***********************************")

#Joins the list of strings into a single string
print(" ".join(str1.strip().split()))

#Counts the number of times the word "New" is present in the string
str1.strip().count("New")

#Prints the index of the first occurence of the word "New" in the string
#Throws Value Error if the word is not present in the string
print(str1.strip().index("Hello"))

#Checks if the string is title case or not
print(str1.strip().istitle())

#Checks if the string is in upper case or not
print(str1.strip().isupper())

#Checks if the string is in lower case or not
print(str1.strip().islower())

#Checks if the string is alphanumeric or not
print(str1.strip().isalnum())

#Checks if the string is a digit or not
print(str1.strip().isdigit())

#Returns -1 if the word is not present in the string
#Returns the index of the first occurence of the word in the string
#We can pass only the word
#Also we can pass the word and the start index and end index position
#Here Start Index is inclusive and End Index is exclusive
print(str1.strip().find("Hello",5,7))

#Swap the cases from capital to small letter
#And Small to Capital Letter
print(str1.strip().swapcase())

#Replace all the letters of 'H' in the given string with another letter 'J'
#Difference between replace and translate is that replace replaces the word with the given word
#Translate replaces the letter with the given letter
print(str1.strip().translate(str.maketrans("H","J")))

#Prints the ASCII value of the first character in the string
print(ord(str1.strip()[0]))

#Prints the character at 4th index position
print(str1.strip()[4])

#Expand Tabs in the string --> Replaces the tab with the given number of spaces
print(str1.strip().expandtabs(2)) #Need to study more on this

#ZFill --> Fills the string with the given number of zeros
#Here we pass the max length of the string
print(str1.strip().zfill(20)) #Need to study more on this

#Prints the first two characters in the string
print(str1.strip()[:2])
