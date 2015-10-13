import pygame

class Moon():
    moonColor = (80, 80, 80);

    def __init__(self, screen, level):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.level = level

    def draw(self):
        rect = (0, self.level, self.width, self.height - self.level)
        pygame.draw.rect(self.screen, self.moonColor, rect, 0)
