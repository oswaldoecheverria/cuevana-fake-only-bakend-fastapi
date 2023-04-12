import requests

REVIEW_ID = 9
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'

REVIEW = {
    'review': "actualizacion",
    'score': 4
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print('La actualizacion fue exitosa')

    print(response.json())

else:
    print(
        response.content
    )