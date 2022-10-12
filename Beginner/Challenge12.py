side1 = input("Enter your first side's length. ")
side2 = input("Enter your second side's length. ")
side3 = input("Enter your third side's length. ")
side4 = input("Enter your fourth side's length. ")

import turtle

window = turtle.Screen()

marty = turtle.Turtle()

#marty.left(180)
#marty.isdown()
marty.forward(float(side1))
marty.left(90)
marty.forward(float(side2))
marty.left(90)
marty.forward(float(side3))
marty.left(90)
marty.forward(float(side4))
marty.left(90)
