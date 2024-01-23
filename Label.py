import pygame

# The class representing a text label
class Label:
    def __init__(self, text, pos, size, colour):
        self.text = text
        self.pos = pos
        self.font = pygame.font.SysFont(None, size)
        self.font_colour = pygame.Color(colour)
        
    def draw(self, screen):
        img = self.font.render(self.text, True, self.font_colour)
        screen.blit(img, self.pos)