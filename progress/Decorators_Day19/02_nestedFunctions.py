def outer():

    def inner():
        print("Inside Inner Function")

    inner()

outer()