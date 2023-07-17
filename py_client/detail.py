import requests

id = input('What is the id of the product?\n')
try:
    id = int(id)
except:
    raise ValueError('not a valid id.') 

endpoint = f'http://127.0.0.1:8000/api/products/{id}/'

get_response = requests.get(endpoint)

print(get_response.json())