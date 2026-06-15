import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

data = response.json()

print(data[0]["name"])