def fizz_buzz (num):
    if num % 3 == 0:
        if num % 5 == 0:
            return "fizzbuzz"
        else:
            return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num
for i in range(1, 4):
    print("Your fizz buzzed number is " + str(fizz_buzz (int(input("What number would you like to fizz buzz?")))))
