import json

#Load method helps in parsing the JSON String and returns the dictionary

with open("example_1.json") as readjson:
    data = json.load(readjson)
    print(data)

    print(data["fruit"])
    print(data["size"])
    #Prints the data type of the data
    print(type(data))

with open("example_2.json") as readcomplexdata:
    data=json.load(readcomplexdata)
    print(data)

    # Access First Question
    print(data["quiz"]["sport"]["q1"]["question"])

    #Access the options
    print(data["quiz"]["sport"]["q1"]["options"])

    #Print second option
    print(data["quiz"]["sport"]["q1"]["options"][1])

    #Print the list of questions
    for question in data["quiz"]["maths"]:

        if question=='q2':
            print(data["quiz"]["maths"][question]["question"])
            print(data["quiz"]["maths"][question]["options"])

            #If it is not matching it throws Assertion Error
            assert data["quiz"]["maths"][question]["question"]=="5 + 7 = ?"

#Difference between load and loads:
# load -> Reads the JSON file and returns the dictionary
# loads -> Reads the JSON String and returns the dictionary