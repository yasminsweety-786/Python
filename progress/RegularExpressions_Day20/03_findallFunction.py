import re

text = "Marks: 85 90 78 95"

numbers = re.findall(r"\d+", text)

print(numbers)