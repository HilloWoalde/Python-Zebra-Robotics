selection = "0"
animal = ""
file=open("62babies.txt", "r")
babies = {
  
}
while True:
    currentLine=file.readline()
    if not currentLine:
        break
    if currentLine != "\n":
        pair=currentLine.split(":")
        babies[pair[0]]=pair[1]
file.close()
while True:
    print("What would you like to do?")
    print("1. Lookup animal baby")
    print("2. Add animal and baby")
    print("3. Delete animal and baby")
    print("4. Save and exit")
    selection = "0"
    selection = input("So, what is it? (1, 2, 3, or 4)")
    if selection == "1":
        animal = input("What animal do you want to know the baby name of?")
        print("The baby of the animal you said is " + babies.get(animal, "not in the list"))
    if selection == "2":
        animal = input("What is the animal")
        babies[animal] = input("What is the baby?")
    if selection == "3":
        animal = input("What animal whose baby would you like to delete")
        del babies[animal]
    if selection == "4":
        file=open("62babies.txt", "w")
        for i in babies:
            file.write(i+":"+babies.get(i)+"\n")
        file.close()
        break

#format of hippo:calf in file:hippo:calf
