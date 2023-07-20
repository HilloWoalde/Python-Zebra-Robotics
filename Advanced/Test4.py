import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((1000,500))

AQUA = [51, 190, 162]

BLACK = [0, 0, 0]

WHITE = [255, 255, 255]

papyrus = pygame.font.Font("Advanced/Fonts/Papyrus.ttf", 20)

quitVar = True

myText = "Hello! Use Space, A Mouse Click, WASD or the Arrow Keys to change the text."
mouseText = "Mouse Position"

while quitVar == True:
    
    screen.fill(BLACK)

    text = papyrus.render(myText, False, WHITE)

    textRect = text.get_rect(center = (500, 205))

    screen.blit(text, textRect)

    text2 = papyrus.render(mouseText, False, WHITE)

    textRect2 = text2.get_rect(center = (600, 305))

    screen.blit(text2, textRect2)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                myText = "Up"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                myText = "Down"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                myText = "Left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                myText = "Right"
            if event.key == pygame.K_SPACE:
                myText = "Space"

        if event.type == pygame.MOUSEBUTTONDOWN:
            myText = "Mouse Click"
        
        mouseText = str(pygame.mouse.get_pos())

    pygame.display.update()

pygame.quit()