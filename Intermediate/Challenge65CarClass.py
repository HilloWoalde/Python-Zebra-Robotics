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
    def stringify(self):
        x=""
        x += ("Make:" + self.Make)
        x += ("\n")
        x += ("Model:" + self.Model)
        x += ("\n")
        x += ("Year:" + self.Year)
        x += ("\n")
        x += ("Price:" + self.Price)
        x += ("\n")
        x += ("Used:" + self.Used)
        x += ("\n")
        x += ("Mileage:" + self.Mileage)
        x += ("\n")
        x += ("Doors:" + self.Doors)
        x += ("\n")
        x += ("Availability:" + self.Available)
        x += ("\n")
        x += ("ID:" + self.ID)
        x += ("\n")
        x += ("\n")
        return(x)
    def printID(self):
        print(self.ID)
    def changeMileage(self):
        self.Mileage = input("What is the car's mileage? (Input a number, like 94500)")
        print(self.Mileage)
    def changeAvailability(self):
        self.Available = input("What is the car's Availability? (Type True for available, False for un-available)")
        print(self.Available)
