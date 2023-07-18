import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((500,500))

image = pygame.image.load("Advanced\Images\Habitica-TransBack.png")

WHITE = [255, 255, 255]

imgX = 0

imgY = 0

FPS = 10000

fpsClock = pygame.time.Clock()

left = 0

down = 0

right = 0

up = 0

quitVar = True

while quitVar == True:

    screen.fill(WHITE)

    screen.blit(image, (imgX, imgY))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    if left <= 300:
        imgY += 1
        left += 1
    
    elif down <= 300:
        imgX += 1
        down += 1

    elif right <= 300:
        imgY -= 1
        right += 1
    
    elif up <= 300:
        imgX -= 1
        up += 1
    
    else:
        imgX = 0
        imgY = 0
        left = 0
        down = 0
        right = 0
        up = 0

    

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()