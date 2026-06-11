import re

text = "Contact: 9876543210"

phone = re.findall(r"\d{10}", text)

print(phone)