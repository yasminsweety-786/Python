class UPI:
    def pay(self):
        print("Paid via UPI")

class Card:
    def pay(self):
        print("Paid via Card")

def checkout(payment):
    payment.pay()

checkout(UPI())
checkout(Card())