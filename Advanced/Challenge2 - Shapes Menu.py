import pygame
import math

def drawRegularPolygon(surface, color, numSides, tiltAngle, x, y, radius):
  pts = []
  for i in range(numSides):
    x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
    y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / numSides)
    pts.append([int(x), int(y)])
  pygame.draw.polygon(surface, color, pts)


while True:

    shape = input("What shape would you like to create? \n  Circle\n  Triangle\n  Square\n  Pentagon\n  Hexagon\n  Octagon\n  Nothing\n   (Case Sensitive)I would like to make:\n   ")

    if shape == "Nothing":
        break

    pygame.init()

    pygame.display.set_caption(shape)

    screen = pygame.display.set_mode ((1000,500))

    AQUA = [51, 190, 162]

    quitVar = True

    while quitVar == True:

        if shape == "Circle":
            pygame.draw.circle(screen, AQUA, (500, 300), 25)
        
        elif shape == "Square":
            pygame.draw.rect(screen, AQUA, (300, 300, 25, 25))

        elif shape == "Triangle":
            pygame.draw.polygon(screen, AQUA, ((300,300),(100,100),(100,300)))

        elif shape == "Pentagon":
            #pygame.draw.polygon(screen, AQUA, ((280,300),(300,100),(250,50),(240,100),(260,390)))
            drawRegularPolygon(screen, AQUA, 5, math.pi / 16, 100, 100, 50)

        elif shape == "Hexagon":
            #pygame.draw.polygon(screen, AQUA, ((280,300),(300,100),(250,50),(240,100),(260,390),(400,400)))
            drawRegularPolygon(screen, AQUA, 6, math.pi / 16, 100, 100, 50)

        elif shape == "Octagon":
            #pygame.draw.polygon(screen, AQUA, ((100, 100),(150, 200),(150, 300),(200, 300),(250, 290),(240, 275),(240, 205),(240, 125)))
            drawRegularPolygon(screen, AQUA, 8, math.pi / 16, 100, 100, 50)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()

    pygame.quit()