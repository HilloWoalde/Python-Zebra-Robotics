import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((750,750))

AQUA = [51, 190, 162]

BLACK = [0, 0, 0]

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

papyrus = pygame.font.Font("Advanced/Fonts/Papyrus.ttf", 20)

quitVar = True

mousePos = (0,0)

img = pygame.image.load("Advanced\Images\AlanBecker-Cursor.png")

img = pygame.transform.scale(img, (50, 50))

mouseX = 0

mouseY = 0

pygame.mouse.set_visible(False)

maze = []

win = "Possible"

pygame.mouse.set_pos(700, 700)

while quitVar == True:    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False
        
        mousePos = pygame.mouse.get_pos()

    mouseX = mousePos[0]

    mouseY = mousePos[1]

    cursRect = pygame.draw.rect(screen, WHITE, ((mousePos), ((mouseX+50),(mouseY+50))))

    screen.fill(WHITE)

    goal = pygame.draw.rect(screen, GREEN, ((0, 0), (50, 50)))

    maze.append(pygame.draw.rect(screen, BLACK, ((0, 50), (1, 100))))

    screen.blit(img, mousePos)

    for i in maze:
        if i.colliderect(cursRect):
            win = "Failed"

    if win != "Failed" and goal.colliderect(cursRect):
        win = ("You Won!")

    if win != "Possible":

        screen.fill(BLACK)

        text = papyrus.render(win, False, WHITE)

        textRect = text.get_rect(center = (500, 205))

        screen.blit(text, textRect)

    #print(win)

    pygame.display.update()

pygame.quit()