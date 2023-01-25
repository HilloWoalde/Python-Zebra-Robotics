import turtle
shape = 0
size = 0
color = ""
def draw(shape=1, size=100, color="black"):
    turtle.pencolor(color)
    if shape==1:
        turtle.circle(size)
    elif shape==2:
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
    elif shape==3:
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)
while True:
    draw(int(input("Circle, Square, or Triangle? 1, 2, or 3?")), int(input("What is the size of your shape?")), input("What is its color?"))
