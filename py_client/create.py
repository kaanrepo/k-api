import requests

#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    'title' : 'My Title 2',
    'price' : 32.98,
    
}

get_response = requests.post(endpoint, json=data)


print(get_response.json())
print(get_response.status_code)