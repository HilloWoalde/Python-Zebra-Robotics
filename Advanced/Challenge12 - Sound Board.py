import pygame

pygame.init()

pygame.display.set_caption("Hello World")

screen = pygame.display.set_mode ((400,200))

AQUA = [51, 190, 162]

BLACK = [0, 0, 0]

WHITE = [255, 255, 255]

RED = [255, 0, 0]

GREEN = [0, 255, 0]

papyrus = pygame.font.Font("Advanced/Fonts/Papyrus.ttf", 20)

songName="\Racing Into The Night Ringtone.mp3"
music = pygame.mixer.Sound("Advanced\Music" + songName)

quitVar = True

song1

while quitVar == True:
    
    music = pygame.mixer.Sound("Advanced\Music" + songName)
    
    screen.fill(WHITE)

    text = papyrus.render("Current Track:", False, BLACK)

    textRect = text.get_rect(center = (200, 20))

    screen.blit(text, textRect)

    text = papyrus.render(songName, False, BLACK)

    textRect = text.get_rect(center = (200, 50))

    screen.blit(text, textRect)

    start = pygame.draw.polygon(screen, GREEN, ((60,150),(15,125),(15,175)))

    stop = pygame.draw.rect(screen, RED, (335,125,50,50))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if start.collidepoint(position):
                music.play()
            elif stop.collidepoint(position):
                music.stop()

    pygame.display.update()

pygame.quit()