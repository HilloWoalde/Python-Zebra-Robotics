import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((1000,500))

AQUA = [51, 190, 162]

BLACK = [0, 0, 0]

WHITE = [255, 255, 255]

papyrus = pygame.font.Font("Advanced/Fonts/Papyrus.ttf", 20)

quitVar = True

while quitVar == True:
    
    screen.fill(BLACK)

    text = papyrus.render("I AM PAPYRUS! NYEH HEH HEH!", False, WHITE)

    textRect = text.get_rect(center = (500, 205))

    screen.blit(text, textRect)

    #pygame.draw.line(screen, WHITE, (275, 125), (725, 125), 4)
    pygame.draw.rect(screen, WHITE, (275,170, 450, 70), 4)

    pygame.draw.circle(screen, AQUA, (500, 300), 25)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit()