import pygame
import random

class StarField:
    white = (255, 255, 255)
    stars = []

    def __init__(self, screen, n = 100):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        for i in range(n):
            self.stars.append((random.randint(0, self.width), random.randint(0, self.height)))

    def update(self):
        pass

    def draw(self):
        for position in self.stars:
            self.screen.set_at(position, self.white)
