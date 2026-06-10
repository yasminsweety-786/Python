def logger(func):

    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")

    return wrapper


@logger
def study():
    print("Studying Python")


study()