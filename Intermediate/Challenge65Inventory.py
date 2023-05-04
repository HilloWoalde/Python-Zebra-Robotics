from Challenge65CarClass import Car
menuoption = ""
allcars=[]
file = open("64Cars.txt", "r")
lines = file.readlines()
carsNum = round(len(lines)/10)-1
for i in range(0, carsNum):
    print(i)
    print(len(lines))
    a = (lines[0+(i*10)].split(":")[1].strip("\n"), lines[1+(i*10)].split(":")[1].strip("\n"), lines[2+(i*10)].split(":")[1].strip("\n"), lines[3+(i*10)].split(":")[1].strip("\n"), lines[4+(i*10)].split(":")[1].strip("\n"), lines[5+(i*10)].split(":")[1].strip("\n"), lines[6+(i*10)].split(":")[1].strip("\n"), lines[7+(i*10)].split(":")[1].strip("\n"), lines[8+(i*10)].split(":")[1].strip("\n"))
    allcars.append(Car(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]))
    
file.close()
while True:
    menuoption = input("Select one option using numbers \n 1.  Find a Car (via id)\n 2.  Add a car \n 3.  I sold a Car! \n 4.  Save and Exit \n 5.  Find a Car ID \n 6.  See all car ID's \n 7.  Update a car's Mileage \n 8.  Update a car's Availability \n P.S.  Please note the ID updates when the program opens, and then is static.")
    if menuoption == "1":
        carToFind = input("What is the ID of the car?")
        for i in allcars:
            if i.ID == carToFind:
                print("Here is the car's values:")
                print(i.stringify())
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
            file.write(i.stringify())
        file.close()
        break
    if menuoption == "5":
        allcars.append(Car(input("What is the car's make? (Input a word, like Nissan)"), input("What is the car's Model? (Input a word, like Rogue)"), input("What is the car's release year? (Input a number, like 2016)"), input("What is the car's price? (Input a number, like 24125)"), input("What is the car's used value? (Type TRUE for used, FALSE for unused)"), input("What is the car's mileage? (Input a number, like 94500)"), input("What is the car's number of doors? (Input a number, like 4)"), input("What is the car's Availability? (Type True for available, False for un-available)")))
        print(allcars[len(allcars)-1].stringify())
        allcars.pop(len(allcars)-1)
    if menuoption == "6":
        for i in allcars:
            i.printID()
    if menuoption == "7":
        carToFind = input("What is the ID of the car you would like to update?")
        for i in allcars:
            if i.ID == carToFind:
                i.changeMileage()
    if menuoption == "8":
        carToFind = input("What is the ID of the car you would like to update?")
        for i in allcars:
            if i.ID == carToFind:
                i.changeAvailability()
