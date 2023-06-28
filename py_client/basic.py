import requests

endpoint = 'https://httpbin.org/anything'

get_response = requests.get(endpoint, json= {'query':'hello q'})

print(get_response.json())