try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError:
    print("Invalid number")

finally:
    print("Program finished")