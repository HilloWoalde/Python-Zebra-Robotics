import pygame
import random

pygame.init()

pygame.display.set_caption("Whack-A-Mole")

screen = pygame.display.set_mode((700, 700))

quitVar = True

WHITE = [255, 255, 255]
AQUA = [51, 190, 162]

score = 0

FPS = 60
fpsClock = pygame.time.Clock()
time = 0

image = pygame.image.load("Advanced\Images\Mole.png")
image = pygame.transform.scale(image, (130, 130))
image_x = random.randint(0, 580)
image_y = random.randint(50, 580)

papyrus = pygame.font.Font("Advanced\Fonts\Papyrus.ttf", 20)

position = [1000, 1000]

while quitVar == True:

    screen.fill(WHITE)

    text = papyrus.render("Score: " + (str)(score), True, AQUA)
    textRect = text.get_rect(center = (50, 10))
    screen.blit(text, textRect)

    screen.blit(image, (image_x, image_y))

    if time % FPS == 0:
        time = 0
        image_x = random.randint(0, 580)
        image_y = random.randint(50, 580)

    if abs(position[0] - (image_x + 60)) <= 60 and abs(position[1] - (image_y + 60)) <= 60:
        time = 0
        score += 1
        image_x = random.randint(0, 580)
        image_y = random.randint(50, 580)
        position = [1000, 1000]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

    pygame.display.update()

    time += 1
    fpsClock.tick(FPS)

pygame.quit()