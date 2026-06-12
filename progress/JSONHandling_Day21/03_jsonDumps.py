import json

student = {
    "name": "Yasmin",
    "age": 20
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))