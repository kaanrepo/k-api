import requests

id = input('What is the id of the product?\n')
try:
    id = int(id)
except:
    raise ValueError('not a valid id.') 

data = {
    'title' : 'a NEW title',
    'content' : 'Is this neccassary?'
}

endpoint = f'http://127.0.0.1:8000/api/products/{id}/update/'
get_response = requests.put(endpoint, data=data)
print(get_response.json())