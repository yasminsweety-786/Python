def decorator(func):

    def wrapper(name):
        print("Welcome")
        func(name)
        print("Goodbye")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Yasmin")