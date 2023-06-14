class Car:
    def __init__(self, Vehicle, Make, Model, Year, Price, Used, Mileage, Doors, Available, ID=""): 
        self.Vehicle = Vehicle
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
        strr=self.Vehicle
        x=[i for i in strr]
        o=str(x[0])
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
        z=o+a+b+c+d+e+f
        self.ID=z

    def stringify(self):
        x=""
        x += ("Vehicle:" + self.Vehicle)
        x += ("\n")
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
        return(x)
    
    def printID(self):
        print(self.ID)


    def changeMileage(self):
        self.Mileage = input("What is the car's mileage? (Input a number, like 94500)")
        print(self.Mileage)


    def changeAvailability(self):
        self.Available = input("What is the car's Availability? (Type True for available, False for un-available)")
        print(self.Available)
        
    
class Motorcycle(Car):
    def __init__(self, Vehicle, Make, Model, Year, Price, Used, Mileage, Doors, Available, ID, Type):
        self.type = Type
        Car.__init__(self, "Motorcycle", Make, Model, Year, Price, Used, Mileage, 0, Available, ID)
    
    def stringify(self):
        return super().stringify() + ("Type:" + self.type) + ("\n")
    
class Truck(Car):
    def __init__(self, Vehicle, Make, Model, Year, Price, Used, Mileage, Doors, Available, ID, Type, Bed):
        self.type = Type
        self.bed = Bed
        Car.__init__(self, "Truck", Make, Model, Year, Price, Used, Mileage, Doors, Available, ID)
        
        

    def stringify(self):
        return super().stringify() + ("Type:" + self.type) + ("\n") + ("Bed:" + self.bed) + ("\n")