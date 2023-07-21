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

songName="Racing Into The Night Ringtone.mp3"
music = pygame.mixer.Sound("Advanced/Music/" + songName)

quitVar = True

song1="Racing Into The Night Ringtone.mp3"
song2="Final Fantasy Main Theme.mp3"
song3="Rush Collection.mp3"
song4="I Built Tears of the Kingdom in Minecraft.mp3"
song5="How Rare Are You.mp3"
song6="When You Dont Skip the Ads.mp3"

while quitVar == True:
    
    screen.fill(WHITE)

    text = papyrus.render("Current Track:", False, BLACK)

    textRect = text.get_rect(center = (200, 20))

    screen.blit(text, textRect)

    text = papyrus.render(songName, False, BLACK)

    textRect = text.get_rect(center = (200, 50))

    screen.blit(text, textRect)

    start = pygame.draw.polygon(screen, GREEN, ((60,110),(15,85),(15,135)))

    stop = pygame.draw.rect(screen, RED, (335,85,50,50))

    st1 = papyrus.render("1", False, BLACK)

    sr1 = st1.get_rect(center = (75, 160))

    screen.blit(st1, sr1)

    st2 = papyrus.render("2", False, BLACK)

    sr2 = st2.get_rect(center = (125, 160))

    screen.blit(st2, sr2)

    st3 = papyrus.render("3", False, BLACK)

    sr3 = st3.get_rect(center = (175, 160))

    screen.blit(st3, sr3)

    st4 = papyrus.render("4", False, BLACK)

    sr4 = st4.get_rect(center = (225, 160))

    screen.blit(st4, sr4)

    st5 = papyrus.render("5", False, BLACK)

    sr5 = st5.get_rect(center = (275, 160))

    screen.blit(st5, sr5)

    st6 = papyrus.render("6", False, BLACK)

    sr6 = st6.get_rect(center = (325, 160))

    screen.blit(st6, sr6)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if sr1.collidepoint(position):
                songName = song1
            if sr2.collidepoint(position):
                songName = song2
            if sr3.collidepoint(position):
                songName = song3
            if sr4.collidepoint(position):
                songName = song4
            if sr5.collidepoint(position):
                songName = song5
            if sr6.collidepoint(position):
                songName = song6
            if start.collidepoint(position):
                music = pygame.mixer.Sound("Advanced/Music/" + songName)
                music.play()
            elif stop.collidepoint(position):
                music.stop()

    pygame.display.update()

pygame.quit()