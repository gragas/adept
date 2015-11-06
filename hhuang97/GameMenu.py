import pygame

class Option:
    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
        
pygame.init()
#make screen bigger if necessary to accommodate more buttons
screen = pygame.display.set_mode((580, 420))
menu_font = pygame.font.Font(None, 40)

"""
--------------------------------------------------------------------------
                        ADD NEW BUTTONS HERE
--------------------------------------------------------------------------
To add a button, use the following format:
Options("INSERT BUTTON NAME HERE", (X_COORDINATE, Y_COORDINATE))
"""

options = [Option("NEW GAME", (140, 105)), Option("LOAD GAME", (135, 155)),
           Option("OPTIONS", (145, 205)), Option("ABOUT", (150,255))]



"""
EDIT BELOW CODE TO ALLOW BUTTON FUNCTIONALITY (e.g. button does something when clocked)
"""

running = True
while running:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
        
    for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                running=False
                break
    pygame.display.update()