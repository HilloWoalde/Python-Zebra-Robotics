destinations = ["Bahamas","Eiffel Tower"]
while True:
    print(destinations)
    num = input("Pick a number from 1 to 5")
    if (num == "1"):
        destinations.append(input("What Destination Would You Like To Add?"))
    elif (num == "2"):
        var = input("What do you want to find?")
        if (destinations.count(var) > 0):
            print(destinations.index(var))
    elif (num == "3"):
        var = input("What do you want to delete?")
        if (destinations.count(var) > 0):
            destinations.remove(var)
    elif (num == "4"):
        destinations = sorted(destinations, key=str.lower)
    elif (num == "5"):
        print(len(destinations))
        
