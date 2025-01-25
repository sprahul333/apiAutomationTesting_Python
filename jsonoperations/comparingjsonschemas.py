import json

with open("example_1.json") as readjson:
    data = json.load(readjson)
    print(data)

with open("example_2.json") as readcomplexdata:
    dataOne=json.load(readcomplexdata)
    print(dataOne)

    #Comparing Two JSON Payloads using the dictionaries
    assert data==dataOne
