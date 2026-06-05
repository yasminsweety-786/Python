class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("Toyota", "Camry")

car1.show()