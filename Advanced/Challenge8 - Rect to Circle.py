import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((500,500))

image = pygame.image.load("Advanced\Images\Habitica-TransBack.png")

WHITE = [255, 255, 255]

AQUA = [51, 190, 162]

imgX = 0

imgY = 0

FPS = 100

fpsClock = pygame.time.Clock()

size = 0

reverse = False

quitVar = True

while quitVar == True:

    screen.fill(WHITE)

    pygame.draw.rect(screen, AQUA, (100, 100, 300, 300))

    pygame.draw.circle(screen, WHITE, (250, 250), 550-size, 300)
    
    if reverse == False:
        size += 1
        if size >= 130:
            reverse = True
    elif reverse == True:
        size -= 1
        if size <= -25:
            reverse = False
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()