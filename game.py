import pygame
from ball import Ball
from button import Button

# General
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Calculus Roll')

# Colors
black = (0,0,0)
white = (255,255,255)

# Display
screen_width = 1280
screen_length = 720

screen = pygame.display.set_mode((screen_width,screen_length))
background = pygame.Surface(screen.get_size())
background.fill(white)
screen.blit(background, (0,0))

# Ball Sprite
ball = Ball(400,200)
sprite_group = pygame.sprite.Group(ball)

# Buttons
button_width = 300
button_height = 50

dif_box = Button(screen_width-button_width-10, 10, button_width, button_height, 'Differentiate')
int_box = Button(screen_width-button_width-10, button_height+20, button_width, button_height, 'Integrate')

buttons = [dif_box,int_box]

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in buttons:
            button.handle_event(event)

    screen.fill(white)

    #sprite_group.clear(screen, background)
    sprite_group.update()
    sprite_group.draw(screen)

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)