import json

students = [
    {"name": "Ali", "marks": 90},
    {"name": "Sara", "marks": 95}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("JSON file created successfully")