import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((500,500))

image = pygame.image.load("Advanced\Images\Habitica-TransBack.png")

WHITE = [255, 255, 255]

imgX = 0

imgY = 0

xVel = 5

yVel = 5

FPS = 100

fpsClock = pygame.time.Clock()

quitVar = True

while quitVar == True:

    screen.fill(WHITE)

    screen.blit(image, (imgX, imgY))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    if imgX < (500-image.get_width()) and imgY < (500-image.get_height()):
        imgX += xVel
        imgY += yVel

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()