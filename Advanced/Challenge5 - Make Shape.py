import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode((1000,500))

GREEN = [0, 255, 0]

BLUE = [0, 0, 255]

WHITE = [255, 255, 255]

quitVar = True

while quitVar == True:
    
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (275,170, 450, 70))
    pygame.draw.rect(screen, GREEN, (275,170, 450, 70), 4)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit()