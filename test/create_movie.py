import requests


URL = 'http://127.0.0.1:8000/api/v1/movies'

MOVIE = {
    'title': "pelicula1"
}

response = requests.post(URL, json=MOVIE)

if response.status_code == 200:
    print('La pelicula fue creada exitosamente')

    print(response.json()['id'])

else:
    print(
        response.content
    )