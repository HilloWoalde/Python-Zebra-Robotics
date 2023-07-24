import pygame

colour = 0,0,0

class Obstacle:
    def __init__(self, x, size, GroundHeight):
        self.x = x
        self.size = size
        self.GroundHeight = GroundHeight

    def draw(self, gameDisplay):
        self.hi = pygame.draw.rect(gameDisplay, colour, [self.x, 360, 20, 20])
        image_x = self.x
        image_y = 360
        cactus = pygame.image.load("Advanced/Images/Cactus.png")
        cactus = pygame.transform.scale(cactus,(20, 20))
        gameDisplay.blit(cactus, (image_x, image_y))
    
    def update(self, deltaTime, velocity):
        self.x -= velocity*deltaTime

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False
        

        