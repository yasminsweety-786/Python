import json

data = '{"name":"Yasmin","age":20}'

python_data = json.loads(data)

print(python_data)
print(type(python_data))