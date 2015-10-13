import pygame
import math

class Lander:
    width = 40
    height = 60
    landerColor = (0, 255, 255)
    thrustColor = (255, 255, 0)
    gravity = 25

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.tx = 0
        self.ty = 0
        self.clock = pygame.time.Clock()

    def setThrustX(self, tx):
        self.tx = tx

    def setThrustY(self, ty):
        self.ty = ty

    def getVelocity(self):
        return math.hypot(self.vx, self.vy)

    def update(self):
        dt = 0.001 * self.clock.tick()
        self.vx += self.tx * dt * 50
        self.vy += self.ty * dt * 50
        self.vy += self.gravity * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        pass

    def draw(self):
        rect = (self.x - self.width / 2, self.y, self.width, -self.height)
        pygame.draw.rect(self.screen, self.landerColor, rect, 0)

        if(self.tx < 0):
            triangle = [
                    (self.x + 20, self.y - 20),
                    (self.x + 30, self.y - 15), 
                    (self.x + 20, self.y - 10), 
                    ]
            pygame.draw.polygon(self.screen, self.thrustColor, triangle)
        elif(self.tx > 0):
            triangle = [
                    (self.x - 20, self.y - 20),
                    (self.x - 30, self.y - 15), 
                    (self.x - 20, self.y - 10), 
                    ]
            pygame.draw.polygon(self.screen, self.thrustColor, triangle)
        if(self.ty < 0):
            triangle = [
                    (self.x - 10, self.y),
                    (self.x, self.y + 20), 
                    (self.x + 10, self.y), 
                    ]
            pygame.draw.polygon(self.screen, self.thrustColor, triangle)



