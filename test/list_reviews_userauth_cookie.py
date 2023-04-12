import requests


URL = 'http://127.0.0.1:8000/api/v1/users/'

QUERYSET = {'page': 1, 'limit': 3}

USER = {
    'username': "oswaldo",
    'password': 'abc123....'
}

response = requests.post(URL + 'login', json=USER)

if response.status_code == 200:
    print('Autenticacion exitosa, bienvenido')

    user_id = response.cookies.get_dict().get('user_id')

    cookies = { 'user_id': user_id }

    response = requests.get(URL + 'reviews', params=QUERYSET, cookies=cookies )

    if response.status_code == 200:
        for review in response.json():
            print(f"> {review['review']} - {review['score']}")

else:
    print(response.content)







