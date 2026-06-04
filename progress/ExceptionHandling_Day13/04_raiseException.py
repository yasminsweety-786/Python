age = int(input("Enter age: "))

if age < 18:
    raise Exception("You must be 18 or older")

print("Access Granted")