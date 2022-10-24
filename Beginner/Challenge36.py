import random
words = ['see','users','user','documents','git','hub','python','beginner','challenge','zebra']
word = random.choice(words)
worlis = list(word)
guess = ""
print("The length of the word is " + str(len(worlis)))
for i in range(1,6):
    guess = input("What is your guess (letter(lowercase))")
    if (guess in worlis):
        print("The letter " + guess + " is in the word.")
    else:
        print("The letter " + guess + " is not in the word.")
guess = input("What do you think the word is?")
if (guess == word):
    print("Congrats! You got the word right!")
else:
    print("Sorry, you got the word wrong.")
