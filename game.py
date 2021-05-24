import pygame
import function
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
screen_length = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_length,screen_height))
background = pygame.Surface(screen.get_size())
background.fill(white)
screen.blit(background, (0,0))

# Functions
functions = ['x^3','sin(x)']
current_function = functions[0]

# Ball Sprite
ball = Ball(400,200)
sprite_group = pygame.sprite.Group(ball)

# Buttons
button_length = 300
button_height = 50

dif_box = Button(screen_length-button_length-10, 10, button_length, button_height, 'Differentiate')
int_box = Button(screen_length-button_length-10, button_height+20, button_length, button_height, 'Integrate')

buttons = [dif_box,int_box]

# Graph
function_graph = pygame.PixelArray(screen)

f = function.function_point(current_function)

for xp in range(screen_length):
    yp = -int(50*f(xp/64))+int(screen_height/2)
    if yp < 0 or yp > screen_height:
        continue
    function_graph[xp][yp] = black

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

        for button in buttons:
            response = button.handle_event(event, current_function)
            if response:
                current_function = response

    '''
    #pygame.display.update()
    
    screen.fill(white)

    #pygame.display.update()

    #sprite_group.clear(screen, background)
    sprite_group.update()
    sprite_group.draw(screen)

    for button in buttons:
        button.draw(screen)

    function_text = font.render(current_function, True, black)
    screen.blit(function_text,(500,10))
    '''

    pygame.display.flip()
    clock.tick(60)