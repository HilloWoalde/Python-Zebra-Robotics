from Challenge65CarClass import Car, Motorcycle, Truck
menuoption = ""
allvehicles=[]
file = open("Intermediate/64Cars.txt")
lines = file.readlines()
vehiclesNum = round(len(lines)/8)
i=0
while True:
    #print(i)
    #print(len(lines))
    print(lines[i])
    vehicle = lines[0+(i)].split(":")[1].strip()
    if vehicle == "Car":
        a = (lines[0+(i)].split(":")[1].strip("\n"), lines[1+(i)].split(":")[1].strip("\n"), lines[2+(i)].split(":")[1].strip("\n"), lines[3+(i)].split(":")[1].strip("\n"), lines[4+(i)].split(":")[1].strip("\n"), lines[5+(i)].split(":")[1].strip("\n"), lines[6+(i)].split(":")[1].strip("\n"), lines[7+(i)].split(":")[1].strip("\n"), lines[8+(i)].split(":")[1].strip("\n"), lines[9+(i)].split(":")[1].strip("\n"))
        allvehicles.append(Car(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9]))
        i+=10
    elif vehicle == "Motorcycle":
        a = (lines[0+(i)].split(":")[1].strip("\n"), lines[1+(i)].split(":")[1].strip("\n"), lines[2+(i)].split(":")[1].strip("\n"), lines[3+(i)].split(":")[1].strip("\n"), lines[4+(i)].split(":")[1].strip("\n"), lines[5+(i)].split(":")[1].strip("\n"), lines[6+(i)].split(":")[1].strip("\n"), lines[7+(i)].split(":")[1].strip("\n"), lines[8+(i)].split(":")[1].strip("\n"), lines[9+(i)].split(":")[1].strip("\n"), lines[10+(i)].split(":")[1].strip("\n"))
        allvehicles.append(Motorcycle(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10]))
        i+=11
    elif vehicle == "Truck":
        a = (lines[0+(i)].split(":")[1].strip("\n"), lines[1+(i)].split(":")[1].strip("\n"), lines[2+(i)].split(":")[1].strip("\n"), lines[3+(i)].split(":")[1].strip("\n"), lines[4+(i)].split(":")[1].strip("\n"), lines[5+(i)].split(":")[1].strip("\n"), lines[6+(i)].split(":")[1].strip("\n"), lines[7+(i)].split(":")[1].strip("\n"), lines[8+(i)].split(":")[1].strip("\n"), lines[9+(i)].split(":")[1].strip("\n"), lines[10+(i)].split(":")[1].strip("\n"), lines[11+(i)].split(":")[1].strip("\n"))
        allvehicles.append(Truck(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11]))
        i+=12
    if i == len(lines):
        #print(lines[i])
        print(lines)
        print(vehicle)
        break

    
file.close()
while True:
    menuoption = input("\n \n \n Select one option using numbers \n 1.  Find a Vehicle (via id)\n 2.  Add a vehicle \n 3.  Update a vehicle's Availability \n 4.  See all vehicle ID's \n 5.  Update a vehicle's Mileage \n 6.  Update a vehicle's Price \n 7.  Save and Exit \n 8.  Exit without saving\n P.S.  Please note the ID updates when the program opens, and then is static. The ID only references The main car class and name of vehicle, no sub class variables such a truck's bed, they will have IDs based off of their car values \n Input your choice here")
    if menuoption == "1":
        vehicleToFind = input("What is the ID of the vehicle?")
        for i in allvehicles:
            if i.ID == vehicleToFind:
                print("Here is the vehicle's values:")
                print(i.stringify())
    if menuoption == "2":
        vehicle = input("What is the vehicle? (Input a word, like Car)")
        if vehicle == "Car":
            allvehicles.append(Car("Car", input("What is the vehicle's make? (Input a word, like Nissan)"), input("What is the vehicle's Model? (Input a word, like Rogue)"), input("What is the vehicle's release year? (Input a number, like 2016)"), input("What is the vehicle's price? (Input a number, like 24125)"), input("What is the vehicle's used value? (Type TRUE for used, FALSE for unused)"), input("What is the vehicle's mileage? (Input a number, like 94500)"), input("What is the vehicle's number of doors? (Input a number, like 4)"), input("What is the vehicle's Availability? (Type True for available, FALSE for un-available)")))
        elif vehicle == "Motorcycle":
            allvehicles.append(Motorcycle("Motorcycle", input("What is the vehicle's make? (Input a word, like Nissan)"), input("What is the vehicle's Model? (Input a word, like Rogue)"), input("What is the vehicle's release year? (Input a number, like 2016)"), input("What is the vehicle's price? (Input a number, like 24125)"), input("What is the vehicle's used value? (Type TRUE for used, FALSE for unused)"), input("What is the vehicle's mileage? (Input a number, like 94500)"),"", input("What is the vehicle's Availability? (Type True for available, FALSE for un-available)"),"", input("What is the vehicle's Type? (Input a word, like Standard)")))
        elif vehicle == "Truck":
            allvehicles.append(Truck("Truck", input("What is the vehicle's make? (Input a word, like Nissan)"), input("What is the vehicle's Model? (Input a word, like Rogue)"), input("What is the vehicle's release year? (Input a number, like 2016)"), input("What is the vehicle's price? (Input a number, like 24125)"), input("What is the vehicle's used value? (Type TRUE for used, FALSE for unused)"), input("What is the vehicle's mileage? (Input a number, like 94500)"), input("What is the vehicle's number of doors? (Input a number, like 4)"), input("What is the vehicle's Availability? (Type True for available, FALSE for un-available)"),"", input("What is the vehicle's Type? (Input a word, like Full Size)"), input("What is the vehicle's Bed? (Input a word, like Long)")))
        allvehicles[len(allvehicles)-1].createID()
        allvehicles[len(allvehicles)-1].printID()
        print("The vehicle's ID is above. Please refer to this for modifications.")
    if menuoption == "3":
        vehicleToFind = input("What is the ID of the vehicle you want to change the availability of?")
        for i in allvehicles:
            if i.ID == vehicleToFind:
                i.changeAvailability(input("What is the car's Availability? (Type True for available, False for un-available)"))
    if menuoption == "4":
        for i in allvehicles:
            i.printID()
    if menuoption == "5":
        vehicleToFind = input("What is the ID of the vehicle you would like to update?")
        for i in allvehicles:
            if i.ID == vehicleToFind:
                i.changeMileage(input("What is the car's mileage? (Input a number, like 94500)"))
    if menuoption == "6":
        vehicleToFind = input("What is the ID of the vehicle you want to change the price of?")
        for i in allvehicles:
            if i.ID == vehicleToFind:
                i.changePrice(input("What is the vehicle's price? (Input a number, like 24125)"))
    if menuoption == "7":
        file=open("64Cars.txt", "w")
        for i in allvehicles:
            file.write(i.stringify())
        file.close()
        break
    if menuoption == "8":
        break