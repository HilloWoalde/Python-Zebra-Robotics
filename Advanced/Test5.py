import pygame
from Test5a import Monster

pygame.init()

pygame.display.set_caption("Game TITLE")

screen = pygame.display.set_mode((1500,850))

FPS = 30
fpsClock = pygame.time.Clock()

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255,0,0]

quitVar = True

myMonsters = []

while quitVar == True: 

    screen.fill(WHITE)
    
    for event in pygame.event.get():
    
        if event.type == pygame.MOUSEBUTTONDOWN:
    
            x,y = pygame.mouse.get_pos() 
            myNewMonster = Monster (x,y) 
        
            myMonsters.append(myNewMonster)
    
    if event.type == pygame.QUIT: 
        quitVar = False
    
    for monstar in myMonsters: 
        monstar.fly (screen)
    
    pygame.display.update() 
    fpsClock.tick(FPS)

pygame.quit()