selection = "0"
animal = ""
babies = {
  "hippo": "calf",
  "horse": "foal",
  "dog": "pup",
  "kangaroo": "joey",
  "monkey": "infant",
  "owl": "owlet",
  "parrot": "chick",
  "rabbit": "bunny",
  "rat": "pup",
  "cow": "calf",
  "skunk": "kit",
  "sheep": "lamb",
}
while True:
    print("What would you like to do?")
    print("1. Lookup animal baby")
    print("2. Add animal and baby")
    print("3. Delete animal and baby")
    selection = "0"
    selection = input("So, what is it? (1, 2, or 3)")
    if selection == "1":
        animal = input("What animal do you want to know the baby name of?")
        print("The baby of the animal you said is " + babies.get(animal, "not in the list"))
    if selection == "2":
        animal = input("What is the animal")
        babies[animal] = input("What is the baby?")
    if selection == "3":
        animal = input("What animal and baby would you like to delete")
        del babies[animal]
