import pygame
from colors import *

gravity = .1

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)

        diameter = 30
        radius = diameter/2
        length = diameter
        height = diameter

        self.image = pygame.Surface((length, height), pygame.SRCALPHA, 32)
        #self.image = self.image.convert_alpha()

        pygame.draw.circle(self.image, black, (radius, radius), radius)
        

        self.rect = self.image.get_rect()
        self.rect.center = (start_x,start_y)
        self.speed = [0,0]

    def update(self):
        if self.rect.center[1] > 345:
            self.speed[1] = -self.speed[1]

        self.speed[1] += gravity
        self.rect = self.rect.move(self.speed)
