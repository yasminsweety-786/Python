class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s1 = Student("Yasmin")
s2 = Student("Ali")
s3 = Student("Sara")

s1.display()
s2.display()
s3.display()