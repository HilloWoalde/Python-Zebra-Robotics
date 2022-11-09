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
    animal = input("What animal do you want to know the baby name of?")
    print("The baby of the animal you said is:" + babies.get(animal, "undefined"))
