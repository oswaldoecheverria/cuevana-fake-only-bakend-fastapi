import requests

URL = 'http://127.0.0.1:8000/api/v1/users'

USER = {
    'username': "cliente2",
    'password': "abc123...."
}

response = requests.post(URL, json=USER)

if response.status_code == 200:
    print('Usuario creado exitosamente')

    print(response.json()['id'])

else:
    print(
        response.content
    )

