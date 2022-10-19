destinations = ["Grapes","Milk (not dad)"]
while True:
    num = input("Pick a number from 1 to 5")
    if (num == "1"):
        destinations.append(input("What Item Would You Like To Add?"))
    elif (num == "2"):
        print(destinations)
    elif (num == "4"):
        var = input("What do you want to delete?")
        if (destinations.count(var) > 0):
            destinations.remove(var)
    elif (num == "3"):
        destinations = sorted(destinations, key=str.lower)
    elif (num == "5"):
        print(len(destinations))
    elif (num == "6"):
        var = input("What do you want to replace?")
        if (destinations.count(var) > 0):
            var = destinations.index(var)
            destinations.remove(var)
        var = input("What do you want to insert in that place??")
            destinations.insert(var)
        
