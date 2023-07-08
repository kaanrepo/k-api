import requests

#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8000/api/'

get_response = requests.post(endpoint, json= {'title': "abc123", 'content':'Hello'})


print(get_response.json())
# print(get_response.headers)
print(get_response.status_code)