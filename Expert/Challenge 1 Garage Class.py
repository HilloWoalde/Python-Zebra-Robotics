from CarClass import Car
caris = []
class garage:
    def __init__(self, cars, floors, space, size):
        self.cars = cars
        self.floors = floors
        self.space = space
        self.size = size

    def __str__(self):
        return "These are the cars in the garage:\n" + str(self.cars) + "." + "\n" + "There are " + str(self.space) + " spaces left in the garage out of " + str(self.size) + " total spaces."

    def __repr__(self):
        return "These are the cars in the garage:\n" + str(self.cars) + "." + "\n" + "There are " + str(self.space) + " spaces left in the garage out of " + str(self.size) + " total spaces."

    def __getitem__(self, item):
        return Garage.cars[item-1]

used = 0
while True:
    if input("Add a vehicle") == "Yes":
        used += 1
        caris.append(Car(input("What vehicle is it?"), input("What is the vehicle's make? (Input a word, like Nissan)"), input("What is the vehicle's Model? (Input a word, like Rogue)"), input("What is the vehicle's release year? (Input a number, like 2016)"), used))
        print("Your parking number is: " + str(used))
    else:
        break
size = int(input("What is the garage size"))
Garage = garage(caris, input("How many floors are there?"), size-used, size)

while True:
    menu = input("1. See Garage \n2. Find a car \n3. Add a Car \n")
    if menu == "1":
        print(Garage)
    elif menu == "2":
        print(Garage[int(input("What is the car's Parking Number?"))])
    elif menu == "3":
        Garage.space -= 1
        Garage.cars.append(Car(input("What vehicle is it?"), input("What is the vehicle's make? (Input a word, like Nissan)"), input("What is the vehicle's Model? (Input a word, like Rogue)"), input("What is the vehicle's release year? (Input a number, like 2016)"), input("What spot is the vehicle parked in? (Input a number, like 5")))
        input("Please insert Card or Cash, or enter management code. Press 'Enter' when done.")