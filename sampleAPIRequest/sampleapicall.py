from http.client import responses

import requests

#Difference between pip install and pip install -U
#pip install -U requests --> This command will update the requests package to the latest version.
#pip install requests --> This command will install the requests package.

#params is used to pass the query parameters in the URL
response=requests.get("http://216.10.245.166/Library/GetBook.php"
             ,params={"AuthorName":"Rahul Shetty2"},
             headers={"Content-Type":"application/json"})

#Content stored in the response
print(response.text)

#Prints the class of Response Object
print(type(response))

#Prints the status code of the response
print(response.status_code)
assert response.status_code==200

#Prints the reason of the status code or Status Line
print(response.reason)

#Convert the response to JSON:
json_response=response.json()
print(json_response)

#Json Response will be stored in the form of List
print(type(json_response))

#Accessing the values from the JSON Response
print(json_response[0]["book_name"])

#Prints the headers of the response
#Returns the headers in the form of Dictionary
print(response.headers)

#Prints the content type of the response
print(response.headers.get("Content-Type"))

assert response.headers.get("Content-Type")=="application/json;charset=UTF-8"

#Retrieve the book with ISBN Name
print(json_response[1]["isbn"])

for book in json_response:
    # print(book["isbn"]) #Prints the isbn of all the books
    if "bcd" in book["isbn"]:
        print(book)
        break
# assert json_response[1]["isbn"]=="bcd"