class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

s1 = Student("Yasmin")

s1.greet()