import requests


data = {
    "title": "Mi primer POST",
    "body": "Estoy aprendiendo APIs",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)
print(response.json())