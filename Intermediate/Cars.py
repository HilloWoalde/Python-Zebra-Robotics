menuoption = ""
allcars=[]
class Car:
    def __init__(self, Make="Cars", Model="Empty", Year=2023, Price=1000, Used=False, Mileage=100, Doors=4, Available=True, ID=""): 
        self.Make = Make
        self.Model = Model
        self.Year = int(Year)
        self.Price = Price
        self.Used = Used
        self.Mileage = Mileage
        self.Doors = Doors
        self.Available = Available
        self.ID = ID

    def createID(self):
        strr=self.Make
        x=[i for i in strr]
        1=str(x[0])
        strr=self.Model
        x=[i for i in strr]
        2=str(x[0])
        intt=self.Year
        x=[i for i in intt]
        3=str(x[2]+x[3])
        intt=self.Price
        4=str(intt/1000)
        intt=self.Mileage
        5=str(intt/100)
        boool=self.Available
        strr=str(boool)
        x=[i for i in strr]
        6=str(x[0])
        z=1+2+3+4+5+6
        print(z)
        self.ID=z
while True:
    currentLine = f.readline()
    if not currentLine:
            break
    line=currentLine.split()
    name=line[0].split(": ")
    name[]=name[0]
    lastName=name[1]
    mark=line[1]
    student = Student(firstName, lastName, "", mark)
    students.append(student)
while True:
    print("Select one option using numbers \n 1.  Find a Car (via id)\n 2.  Add a car \n 3.  I sold a Car! \n  4. Save and Exit")
    if menuoption = 1:
        input("Please enter the ID of the Car.")
        for i in students:
            if (i.firstName == studentToFind):
                newMark = input("What is the student's new grade? ")
                i.setMark(newMark)
