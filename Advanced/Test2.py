import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((500,500))

habitica = pygame.image.load("Advanced\Images\Habitica-TransBack.png")

WHITE = [255, 255, 255]

imgX = 0

imgY = 0

FPS = 45

fpsClock = pygame.time.Clock()

quitVar = True

while quitVar == True:

    screen.fill(WHITE)

    screen.blit(habitica, (imgX, imgY))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    if imgX and imgY == 500:
        imgX = -200
        imgY = -200

    imgX += 1

    imgY += 1

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()