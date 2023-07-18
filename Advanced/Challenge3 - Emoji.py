import pygame

pygame.init()

pygame.display.set_caption("Emoji")

screen = pygame.display.set_mode ((1000,500))

papyrus = pygame.font.Font("Advanced/Fonts/Emoji.ttf", 20)

YELLOW = [255,222,52]

WHITE = [255, 255, 255]

BROWN = [142, 88, 62]

RED = [255, 0, 0]

quitVar = True

while quitVar == True:

    text = papyrus.render("🥳🧁🍰🎁🎂🎈🎺🎉🎊📧〽️", True, WHITE)

    textRect = text.get_rect(center = (500, 205))
    
    pygame.draw.circle(screen, YELLOW, (500, 300), 25)

    pygame.draw.line(screen, BROWN, (484, 290), (494, 290), 4)

    pygame.draw.line(screen, BROWN, (516, 290), (506, 290), 4)

    pygame.draw.line(screen, BROWN, (494, 310), (506, 310), 8)

    pygame.draw.line(screen, BROWN, (491, 310), (509, 310), 4)

    pygame.draw.line(screen, RED, (494, 310), (506, 310), 2)

    screen.blit(text, textRect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit()