menuoption = ""
allcars=[]
class Car:
    def __init__(self, Make="Cars", Model="Empty", Year="2023", Price="1000", Used="False", Mileage="100", Doors="4", Available="True", ID=""): 
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Price = Price
        self.Used = Used
        self.Mileage = Mileage
        self.Doors = Doors
        self.Available = Available
        self.ID = ID
        self.createID()

    def createID(self):
        strr=self.Make
        x=[i for i in strr]
        a=str(x[0])
        strr=self.Model
        x=[i for i in strr]
        b=str(x[0])
        intt=self.Year
        x=[i for i in intt]
        c=str(x[2]+x[3])
        intt=self.Price
        d=str(int(int(intt)/1000))
        intt=self.Mileage
        e=str(int(int(intt)/100))
        boool=self.Available
        strr=str(boool)
        x=[i for i in strr]
        f=str(x[0])
        z=a+b+c+d+e+f
        #print(a)
        #print(b)
        #print(c)
        #print(d)
        #print(e)
        #print(f)
        #print(z)
        self.ID=z
    def printMe(self):
        print("Make:" + self.Make)
        print("Model:" + self.Model)
        print("Year:" + self.Year)
        print("Price:" + self.Price)
        print("Used:" + self.Used)
        print("Mileage:" + self.Mileage)
        print("Doors:" + self.Doors)
        print("Availability:" + self.Available)
        print("ID:" + self.ID)
    def printID(self):
        print(self.ID)
file = open("64Cars.txt", "r")
lines = file.readlines()
carsNum = round(len(lines)/10)
for i in range(0, carsNum):
    allcars.append(Car(lines[0+(i*10)].split()[1], lines[1+(i*10)].split()[1], lines[2+(i*10)].split()[1], lines[3+(i*10)].split()[1], lines[4+(i*10)].split()[1], lines[5+(i*10)].split()[1], lines[6+(i*10)].split()[1], lines[7+(i*10)].split()[1], lines[8+(i*10)].split()[1]))
while True:
    menuoption = input("Select one option using numbers \n 1.  Find a Car (via id)\n 2.  Add a car \n 3.  I sold a Car! \n 4.  Save and Exit \n 5.  Find a Car ID \n 6.  See all car ID's \n")
    if menuoption == "1":
        carToFind = input("What is the ID of the car?")
        for i in allcars:
            if i.ID == carToFind:
                print("Here is the car's values:")
                i.printMe()
    if menuoption == "2":
        allcars.append(Car(input("What is the car's make? (Input a word, like Nissan)"), input("What is the car's Model? (Input a word, like Rogue)"), input("What is the car's release year? (Input a number, like 2016)"), input("What is the car's price? (Input a number, like 24125)"), input("What is the car's used value? (Type TRUE for used, FALSE for unused)"), input("What is the car's mileage? (Input a number, like 94500)"), input("What is the car's number of doors? (Input a number, like 4)"), input("What is the car's Availability? (Type True for available, FALSE for un-available)")))
        allcars[len(allcars)-1].printID()
    if menuoption == "3":
        carToFind = input("What is the ID of the car you sold?")
        for i in allcars:
            if i.ID == carToFind:
                i.Available = False
    if menuoption == "4":
        file=open("64Cars.txt", "w")
        for i in allcars:
            file.write("Make: " + i.Make)
            file.write("\n")
            file.write("Model: " + i.Model)
            file.write("\n")
            file.write("Year: " + i.Year)
            file.write("\n")
            file.write("Price: " + i.Price)
            file.write("\n")
            file.write("Used: " + i.Used)
            file.write("\n")
            file.write("Mileage: " + i.Mileage)
            file.write("\n")
            file.write("Doors: " + i.Doors)
            file.write("\n")
            file.write("Availability: " + i.Available)
            file.write("\n")
            file.write("ID: " + i.ID)
            file.write("\n")
            file.write("\n")
        file.close()
        break
    if menuoption == "5":
        allcars.append(Car(input("What is the car's make? (Input a word, like Nissan)"), input("What is the car's Model? (Input a word, like Rogue)"), input("What is the car's release year? (Input a number, like 2016)"), input("What is the car's price? (Input a number, like 24125)"), input("What is the car's used value? (Type TRUE for used, FALSE for unused)"), input("What is the car's mileage? (Input a number, like 94500)"), input("What is the car's number of doors? (Input a number, like 4)"), input("What is the car's Availability? (Type True for available, FALSE for un-available)")))
        allcars[len(allcars)-1].printMe()
        allcars.pop(len(allcars)-1)
    if menuoption == "6":
        for i in allcars:
            i.printID()
