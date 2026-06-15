import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
)

todo = response.json()

print("Title:", todo["title"])
print("Completed:", todo["completed"])