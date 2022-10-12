import random #imports code
#rand = random.randint(1,6) #random number from 1-5 #Does 1-6?? Ask Coach Rajath
rand = random.randint(1,5) #random number from 1-5 #works i think?
print(rand)
guess = input("guess a number from 1-5") #guess input
print(guess)
if (int(guess)==int(rand)):
    print("Good Job! You got it correct!")
#
elif (int(guess)>int(rand)):
    print("It's too big!")
    guess = input("guess a number from 1-5") #guess input
    if (int(guess)==int(rand)):
        print("Good Job! You got it correct!")
    elif (int(guess)>int(rand)):
        print("It's too big!")
        guess = input("guess a number from 1-5") #guess input
        if (int(guess)==int(rand)):
            print("Good Job! You got it correct!")
        elif (int(guess)>int(rand)):
            print("You Failed.")
        elif (int(guess)<int(rand)):
            print("You Failed.")    
    elif (int(guess)<int(rand)):
        print("It's too small!")
        guess = input("guess a number from 1-5") #guess input
        if (int(guess)==int(rand)):
            print("Good Job! You got it correct!")
        elif (int(guess)>int(rand)):
            print("You Failed.")
        elif (int(guess)<int(rand)):
            print("You Failed.")
#
elif (int(guess)<int(rand)):
    print("It's too small!")
    guess = input("guess a number from 1-5") #guess input
    if (int(guess)==int(rand)):
        print("Good Job! You got it correct!")
    elif (int(guess)>int(rand)):
        print("It's too big!")
        guess = input("guess a number from 1-5") #guess input
        if (int(guess)==int(rand)):
            print("Good Job! You got it correct!")
        elif (int(guess)>int(rand)):
            print("You Failed.")
        elif (int(guess)<int(rand)):
            print("You Failed.")    
    elif (int(guess)<int(rand)):
        print("It's too small!")
        guess = input("guess a number from 1-5") #guess input
        if (int(guess)==int(rand)):
            print("Good Job! You got it correct!")
        elif (int(guess)>int(rand)):
            print("You Failed.")
        elif (int(guess)<int(rand)):
            print("You Failed.")
#
#elif (int(guess)==int(rand)):
    #print("You got it wrong, good luck next time.")
#
