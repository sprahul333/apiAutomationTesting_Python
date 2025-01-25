import requests

url="https://api.github.com/user"

#This is how we pass the username and password for authentication
#Auth allows the data in the form of tuples
#Verify=False is used to ignore the SSL Certificate
responseCode=requests.get(url,verify=False,auth=('sprahul333@gmail.com','2042rahu@6676P'))

print(responseCode.status_code)