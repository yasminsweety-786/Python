class Bird:
    def fly(self):
        print("Bird flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

def let_it_fly(obj):
    obj.fly()

let_it_fly(Bird())
let_it_fly(Airplane())