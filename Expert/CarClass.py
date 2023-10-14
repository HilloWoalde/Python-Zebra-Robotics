class Car:
    def __init__(self, Vehicle, Make, Model, Year, number): 
        self.Vehicle = Vehicle
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Number = number

    def stringify(self):
        x="\n"
        x += ("Vehicle:" + self.Vehicle)
        x += ("\n")
        x += ("Make:" + self.Make)
        x += ("\n")
        x += ("Model:" + self.Model)
        x += ("\n")
        x += ("Year:" + self.Year)
        x += ("\n")
        x += ("Parking Number:" + str(self.Number))
        x += ("\n")
        return(x)

    def __str__(self):
        return self.stringify()
    
    def __repr__(self):
        return self.stringify()