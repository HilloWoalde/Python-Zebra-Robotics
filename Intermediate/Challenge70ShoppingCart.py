#Initialization
import random

tax = 0.13

items = []


#Class for the Cart

class ShoppingCart:

    def __init__(self):

        #Number of items in the shopping cart

        self.numOfItems = 0

        #Names of items in the cart

        self.cart = []

        #Total before tax

        self.subtotal = 0.0

        #Amount to be paid for tax

        self.taxPrice = 0.0

        #Total after tax

        self.total = 0.0

    #Function to add an item to the user's cart

    def addItem(self, name, price, amount):

        for b in range(amount):

            self.numOfItems += 1

            self.cart.append(name)

            self.subtotal += price

            self.taxPrice = round((self.subtotal * tax), 2)

            self.total= self.subtotal + self.taxPrice

    def CartPrinter(self):
        x=""
        for i in self.cart:
            x += "\n " + i
        return "There are " + str(self.numOfItems) + " items in your cart. These are what they are." + x

    def MoneyPrinter(self):
        return "Here is the price of everything in your cart. \n Subtotal: " + str(self.subtotal) + "\n Tax: " + str(self.taxPrice) + "\n Total: " + str(self.total) + "\n"
    
    def Reset(self):
        self.numOfItems = 0

        self.cart = []

        self.subtotal = 0.0

        self.taxPrice = 0.0

        self.total = 0.0

#Class for items the user can buy

class item():

    def __init__(self, name, price, size, id = random.randint(0, 50)):
        self.name = name
        self.price = float(price)

        self.size = size

        x = id

        while True:

            a = 0

            for i in items:

                if i.id != x:

                    a += 1

            if a == len(items):

                break

            x = random.randint(0, 50)

        self.id = x


    #Function to print item information

    def printer(self):

        return " Item Name: " + self.name + "\n Item Price: " + str(self.price) + "\n Item Size: " + self.size + "\n Item ID: " + str(self.id) + "\n"


#Create a shopping cart for a user

Cart = ShoppingCart()


#Creating items the user can buy

items.append(item("Milk", 5.89, "4 L", 1))

items.append(item("Bread", 5.29, "680 g"))

items.append(item("Galaxy S23 Ultra", 5.89, "1 Phone"))

items.append(item("Microsoft 365 Personal Subscription", 79.00, "1 Person, 1 TB"))

items.append(item("Glass Dry Erase Whiteboard", 2030.00, "6 * 4'"))

items.append(item("3D Printer", 132500.00, "1 Printer"))



print("\nHere are some items you can buy. \n")

for i in items:
    x = random.randint(0,1)
    y = random.randint(0,1)
    if x == y:
        print(i.printer())


#Menu


while True:
    menuoption = input("Select one option using numbers \n 1.  Add an item to cart\n 2.  Buy items in your cart\n 3.  View your cart's subtotal, tax, and total \n 4.  View all items \n 5.  Clear Shopping Cart \n 6.  Add an item \n 7.  View items in cart \n 8.  Exit without buying anything\n ")
    if menuoption == "1":

        ask = input("What is the id of the item?")

        for i in items:

            if i.id == int(ask):
                print(i.printer())

                ask = input("How much of this item would you like to buy?")

                Cart.addItem(i.name, i.price, int(ask))

    if menuoption == "2":
        print("This is your cart.")
        print(Cart.CartPrinter())
        print(Cart.MoneyPrinter())
        input("Please input your card information, and wait for the purchasing screen to say transaction complete. You may then press enter to end the program")
        break

    if menuoption == "3":
    
        print(Cart.MoneyPrinter())
    
    if menuoption == "4":
        
        print("These are all possible items you can buy. \n")

        for i in items:
            print(i.printer())

    if menuoption == "5":
        
        Cart.Reset()

    if menuoption == "6":
        
        Thing = item(input("What is the name of the object you would like to be able to buy? (e.g. Milk)"), input("What is the price of the object you would like to buy? (e.g. 5.89)"), input("What is the quantity of the object you would like to buy? (e.g. 4 L)"))

        items.append(Thing)

    if menuoption == "7":

        print(Cart.CartPrinter())

    if menuoption == "8":

        break
