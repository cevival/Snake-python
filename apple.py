import pygame
import random
class Apple:
    def __init__ (self, apple_color):
        self.apple_color = (255,120,0) #De tête
        

    def draw(self, screen,  tilesize):
        for _ in 3:
            apple_posX = random.randint(1, 20)
            apple_posY = random.randint(1, 10)
            pygame.draw.circle(screen, self.apple_color, (apple_posX, apple_posY),  tilesize, 2 )