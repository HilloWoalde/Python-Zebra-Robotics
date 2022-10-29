import random
words = ['see','users','user','documents','git','hub','python','beginner','challenge','zebra']
word = random.choice(words)
worlis = list(word)
index = 0
guess = ""
guelis = []
badlets = []
trilef = 5
for i in worlis:
    guelis += "_"
print("The length of the word is " + str(len(worlis)))
while trilef > 0 and "_" in guelis:
    if ("_" in guelis):
        guess = input("What is your guess (letter(lowercase))")
        if (guess in worlis):
            while (guess in worlis):
            #print("The letter " + guess + " is in the word.")
            #count = 0
            #worlis.count(guess)
                for i in worlis:
                    if (guess == i):
                        index = worlis.index(guess)
                        worlis.pop(index)
                        worlis.insert(index, "*")
                        guelis.pop(index)
                        guelis.insert(index, guess)
                        

        else:
            if (guess != worlis and guess != guelis):
                print("The letter " + guess + " is not in the word.")
                badlets.append(guess)
                trilef -= 1
        print(guelis)
        print("You're incorrect guesses are: " + str(badlets))
        print("You have " + str(trilef) + " tries left")
        
if ("_" in guelis):
    #guess = input("What do you think the word is?")
    #if (guess == word):
        #print("Congrats! You got the word right!")
    #else:
        #print("Sorry, you got the word wrong.")
#else:
    #print("Congrats! You got the word!")
    print("You died.")
else:
    print("You won!")
