try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))

    result = num1 / num2

    print("Result =", result)

except ValueError:
    print("Only numbers allowed")

except ZeroDivisionError:
    print("Division by zero is not allowed")

finally:
    print("Thank you for using calculator")