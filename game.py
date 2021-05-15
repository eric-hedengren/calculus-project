import pygame
from ball import Ball

# General
clock = pygame.time.Clock()

# Display
pygame.display.set_caption('Calculus Roll')

screen = pygame.display.set_mode((1280,720))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
screen.blit(background, (0, 0))

# Ball Sprite
ball = Ball(400,200)
sprite_group = pygame.sprite.Group(ball)

# Main Loop
running = True
while running:
    sprite_group.clear(screen, background)
    sprite_group.update()
    sprite_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False