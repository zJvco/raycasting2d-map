import pygame


class Tile:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size), 1)
