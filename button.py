import pygame

pygame.init()
font = pygame.font.Font(None, 50)
black = (0,0,0)

class Button:
    def __init__(self, x, y, w, h, template):
        self.rect = pygame.Rect(x, y, w, h)
        self.active = False
        self.template = template
        self.text = ''

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_ESCAPE:
                    self.active = False

                elif event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    self.text += event.unicode

    def draw(self, screen):
        if self.active:
            self.txt_surface = font.render(self.text, True, black)
        else:
            self.txt_surface = font.render(self.template, True, black)

        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5)) # center text 
        pygame.draw.rect(screen, black, self.rect, 5)