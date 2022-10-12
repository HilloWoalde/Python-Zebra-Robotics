height = input("What is your height (in inches ONLY, and only numbers)?")
#print()
if (float(height) >= 54):
    print("You are permitted to ride All of our rides.")
#
elif(float(height) >= 48):
    print("You are permitted to ride Vortex, Lumber Jack, Flying Canoes, Tree Top Adventure, Taxi Jam, and Sugar Shack, but can't ride Flight Deck, Behemoth, and Leviathan.")
#
elif(float(height) >= 40):
    print("You are permitted to ride Tree Top Adventure, Taxi Jam, and Sugar Shack, but can't ride Vortex, Lumber Jack, Flying Canoes, Flight Deck, Behemoth, and Leviathan.")
#
else:
    print("I'm sorry little one, but you may not ride any of our rides.")
