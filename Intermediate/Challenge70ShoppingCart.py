tax = 0.13
items = []
class ShoppingCart:
    def __init__(self):
        #Number of items in the shopping cart
        self.numOfItems = 0
        #Names of items in the cart
        self.cart = []
        #Total before tax
        self.subtotal = 0
        #Amount to be paid for tax
        self.taxPrice = 0
        #Total after tax
        self.total = 0
    
    def addItem(self, name, price, amount):
        for i in int(amount):
            self.numOfItems += 1
            self.cart.append(name)
            self.subtotal += int(price)
            self.tax = self.subtotal * tax
            self.total= self.subtotal + self.tax

class item():
    def __init__(self, name, price, size):
        self.name=name
        self.price=int(price)
        self.size=size
    
    def printer(self):
        return " Item Name: " + self.name + "\n Item Price: " + str(self.price) + "\n Item Size: " + self.size + "\n"


Cart = ShoppingCart()

Milk = item("Milk", 5.89, "4 L")
Bread = item("Bread", 5.29, "680 g")
items.append(Milk)
items.append(Bread)

print("\nHere are some items you can buy. \n")
for i in items:
    print(i.printer())