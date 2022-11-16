import math
def sped_test (speed):
    points = 0
    points += math.floor((speed-70)/5)
    if points < 1:
        return "Ok"
    elif points < 13:
        return "Your demerit points are is: " + str(points)
    elif points > 12:
        return "License Suspended"
    else:
        return "Error"
while True:
    print(sped_test(int(input("What is your driving speed"))))
