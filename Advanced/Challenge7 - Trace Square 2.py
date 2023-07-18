import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((500,500))

image = pygame.image.load("Advanced\Images\Habitica-TransBack.png")

WHITE = [255, 255, 255]

imgX = 0

imgY = 0

FPS = 1000

fpsClock = pygame.time.Clock()

a = 0

b = 0

c = 0

d = 0

quitVar = True

while quitVar == True:

    screen.fill(WHITE)

    screen.blit(image, (imgX, imgY))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    if a <= 300:
        imgX += 1
        a += 1
    
    elif b <= 300:
        imgX -= 1
        imgY += 1
        b += 1

    elif c <= 300:
        imgX += 1
        c += 1
    
    elif d <= 300:
        imgX -= 1
        imgY -= 1
        d += 1
    
    else:
        imgX = 0
        imgY = 0
        a = 0
        b = 0
        c = 0
        d = 0

    

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()