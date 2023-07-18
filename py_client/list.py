import requests
from getpass import getpass

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'

username = input('Enter your username.\n')
password = getpass('Enter your password.\n')

auth_response = requests.post(auth_endpoint, json={
    'username' : username ,
    'password': password
    })

if auth_response.status_code == 200:
    print('Authorization successful.')
    auth_token = auth_response.json().get('token')
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    endpoint = 'http://127.0.0.1:8000/api/products/'
    get_response = requests.get(endpoint, headers=headers)
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print(results)
    print(f'Next Url:{next_url}')
else:
    print(auth_response.text)
