import requests

from sampleAPIRequest import payload
from utilities import configurations
from utilities.resources import Resources

# responseData=requests.post("http://216.10.245.166/Library/Addbook.php",json={
#     "name":"Learn PLaywright Automation with Java",
# "isbn":"ISBN92894824",
# "aisle":230,
# "author":"Kumaran"
# }, headers={"Content-Type":"application/json"})

postURL=configurations.get_base_url()+Resources.addEndPoint
deleteURL=configurations.get_base_url()+Resources.deleteEndPoint
headersData={"Content-Type":"application/json"}
responseData=requests.post(postURL
                ,json=payload.jsonPayload("Automation Fundamentals","ISBN00000394","Toni Anand"),
                headers=headersData)
print(responseData.status_code)
assert responseData.status_code == 200

# print(responseData.json())

#Fetch the Book ID
bookId=responseData.json()["ID"]
msg=responseData.json()["Msg"]

if msg == 'Book Already Exists':
    print("Book Already Exists, so not continuing with the Delete Operation")
    exit() #Stop the executing immediately

print("Book ID is",bookId)

deleteResponse=requests.post(deleteURL,json ={
    "ID":bookId
}, headers={"Content-Type":"application/json"})

#Prints the status code
print(deleteResponse.status_code)

#Prints the JSON Response of the Delete Request
#print(deleteResponse.text)