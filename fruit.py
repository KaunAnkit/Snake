import pygame
import random
from pygame.math import Vector2

class FRUITS:
    def __init__(self, cell_number, cell_size):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()
        self.randomise()

    def draw_fruit(self, screen):
        fruit_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, 
                                self.cell_size, self.cell_size)
        screen.blit(self.apple, fruit_rect)

    def randomise(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)