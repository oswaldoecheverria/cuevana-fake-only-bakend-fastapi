import requests

REVIEW_ID = 9
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.delete(URL)

if response.status_code == 200:
    print('Se elimino correctamente')

else:
    print(
        response.content
    )