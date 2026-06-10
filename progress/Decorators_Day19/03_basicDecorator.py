def decorator(func):

    def wrapper():
        print("Before Function Call")
        func()
        print("After Function Call")

    return wrapper


@decorator
def greet():
    print("Hello!")


greet()