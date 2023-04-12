import requests


URL = 'http://127.0.0.1:8000/api/v1/movies'

HEADERS = { 'accept': 'application/json' }
response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    print('Peticion realizada de forma exitosa')

    if response.headers.get('content-type') == 'application/json':
        
        movies = response.json()

        for movie in movies:
            print(f"> id: {movie['id']} - titulo: {movie['title']}")
        