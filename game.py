import pygame
import calculate
from colors import *
from ball import Ball
from button import Button

# General
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
pygame.display.set_caption('Calculus Roll')

# Display
screen_length = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_length,screen_height))
background = pygame.Surface(screen.get_size())
background.fill(white)
screen.blit(background, (0,0))

# Functions
functions = ['-x^(1/2)','sin(x)','x^2','0']
current_function = functions[3]

# Ball Sprite
ball = Ball(screen_length/2,250)
sprite_group = pygame.sprite.Group(ball)

# Buttons
button_length = 300
button_height = 50

dif_box = Button(screen_length-button_length-10, 10, button_length, button_height, 'Differentiate')
int_box = Button(screen_length-button_length-10, button_height+20, button_length, button_height, 'Integrate')

buttons = [dif_box,int_box]

# Graph
def new_graph(function):
    graph = pygame.Surface((screen_length, screen_height), pygame.SRCALPHA, 32)
    #graph.fill(white)
    f = calculate.function_point(function)

    def calc_y(x):
        return -(int(50*f(x/400)))+int(screen_height/2)

    x1 = 1
    y1 = calc_y(x1)

    for x2 in range(2,screen_length):
        y2 = calc_y(x2)
        if y1 < 0 and y1 > screen_height and y2 < 0 and y2 > screen_height:
            continue
        elif 0 < y1 < screen_height and y2 < 0:
            y2 = 0
        elif 0 < y1 < screen_height and y2 > screen_height:
            y2 = screen_height-1
        elif 0 < y2 < screen_height and y1 < 0:
            y1 = 0
        elif 0 < y2 < screen_height and y1 > screen_height:
            y1 = screen_height-1


        pygame.draw.line(graph, black, (x1,y1),(x2,y2))
        x1 = x2
        y1 = y2

    return graph

graph = new_graph(current_function)


# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

        for button in buttons:
            response = button.handle_event(event, current_function)
            if response:
                current_function = response
                graph = new_graph(current_function)

    screen.fill(white)

    screen.blit(graph,(0,0))

    #sprite_group.clear(screen, background)
    sprite_group.update()
    sprite_group.draw(screen)

    for button in buttons:
        button.draw(screen)

    function_text = font.render(current_function, True, black)
    screen.blit(function_text,(500,10))

    pygame.display.flip()
    clock.tick(60)