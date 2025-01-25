import requests

responseData=requests.post("http://216.10.245.166//Library/Addbook.php",json={
    "name":"Learn PLaywright Automation with Java",
"isbn":"gjsdhbgdsr",
"aisle":229,
"author":"Kumar"
}, headers={"Content-Type":"application/json"})

print(responseData.status_code)
assert responseData.status_code == 200

print(responseData.json())

#Fetch the Book ID
bookId=responseData.json()["ID"]

print("Book ID is",bookId)

