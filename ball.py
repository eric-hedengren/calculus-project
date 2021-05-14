import pygame

gravity = .5

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)

        diameter = 30
        radius = diameter/2
        width = diameter
        height = diameter

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))

        pygame.draw.circle(self.image, (0,0,0), (radius, radius), radius)

        self.rect = self.image.get_rect()
        self.rect.center = (start_x,start_y)
        self.speed = [0,0]

    def update(self):
        self.speed[1] += gravity
        self.rect = self.rect.move(self.speed)