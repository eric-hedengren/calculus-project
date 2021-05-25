import pygame
from colors import *

gravity = .5

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

    def update(self, collision):
        if self.rect.center[1]+15 >= collision[1]:
            self.speed[1] = -self.speed[1]
            if self.rect.center[1]+15 >= collision[1]+5:
                self.speed[1] = 0

        self.speed[1] += gravity
        self.rect = self.rect.move(self.speed)
