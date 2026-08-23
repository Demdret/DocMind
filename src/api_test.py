import os
import requests

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "title": "El grande mundo de papurrinsin",
    "body": "Papurrinsin es un niño muy curioso le encantan las computadoras, aunque no cuenta con los recursos adecuados para ser el mejor programador del mundo, aún así se esfuerza demasido por ser mejor cada día.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers,
    json=data
)

data = response.json()

print(response.status_code)
print(f"El id del post es: {data['id']}")
print(f"El titulo del post es: {data['title']}")
print(f"El cuerpo del post es: {data['body']}")