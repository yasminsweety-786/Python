import json

student = {
    "name": "Yasmin",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)