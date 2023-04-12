import requests


URL = 'http://127.0.0.1:8000/api/v1/reviews'

REVIEW = {
    'user_id': 4,
    'movie_id': 1,
    'review': "reviewew",
    'score': 3 
}

response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print('Reseña creada exitosamente')
    
    print(response.json()['id'])

else:
    print(
        response.content
    )