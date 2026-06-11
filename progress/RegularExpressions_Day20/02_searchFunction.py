import re

text = "My number is 9876543210"

result = re.search(r"\d+", text)

print(result.group())