import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)


data = response.json()
print(f"El código de la petición solicitada es: {response.status_code}")
print(f"El nombre del primer usuario es: {data[0]["name"]}")
print(f"El email del primer usuaruio es: {data[0]["email"]}")
