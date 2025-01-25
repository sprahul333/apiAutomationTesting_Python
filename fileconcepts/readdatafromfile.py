#Open --> Opening the file via Python
#If the file is not present, it will throw FileNotFoundError

try:
    f1=open("read.txt")
except FileNotFoundError:
    f1=open("read.txt","w")
    f1.write("Sample Data,Hello World,New World in Making")
    f1=open("read.txt")

#Read all the contents of the file
# print(f1.read())

#REading first five characters of the file
#print(f1.read(5))

#Reading the file line by line
#.readLine() will read the first line of the file
#print(f1.readline())

#Print the whole data using .readLine() method

#Reading the whole file using while loop
# data=f1.readline()
#
# while data!="": #When data is empty, it will return False that means we have reached the end of the file
#     print(data)
#     data=f1.readline()

#Each and every line will be stored in a list
#print(f1.readlines())

for line in f1.readlines():
    print(line)

f1.close() #To Close the file operations