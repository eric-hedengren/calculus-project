import pygame
from ball import Ball
from button import Button

# General
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
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

# Functions
functions = ['x^3','sin(x)']
current_function = functions[1]

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
            response = button.handle_event(event, current_function)
            if response:
                current_function = response

    screen.fill(white)

    #sprite_group.clear(screen, background)
    sprite_group.update()
    sprite_group.draw(screen)

    for button in buttons:
        button.draw(screen)

    function_image = font.render(current_function, True, black)
    screen.blit(function_image,(500,10))

    pygame.display.flip()
    clock.tick(60)