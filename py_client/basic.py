import requests

#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8000/'

get_response = requests.get(endpoint, json= {'query':'hello q'})

print(get_response.json())

print(get_response.status_code)