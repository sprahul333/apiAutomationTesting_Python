with open("dummy.txt","w") as writeMode: #In this way, the file object gets closed automatically
    writeMode.write("Hello World,New World in Making")
    writeMode.writelines("\nVirat Kohli is the best cricketer in the world")

#Reverse each and every line of data that is present in the file

with open("dummy.txt","r") as readmode:
    completeContent=readmode.readlines()

    reversed(completeContent)

    with open("reversedFile.txt","w") as reverseWriteMode:
        for line in completeContent:
            reverseWriteMode.write(line)