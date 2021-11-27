from os import get_terminal_size
import pygame
from pygame import display

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, velocity, display):
        super().__init__()
        self.display_surface = display
        self.image = pygame.Surface((size, size))
        self.image.fill('purple')
        self.rect = self.image.get_rect(topleft = pos)
        self.vel = velocity

    def draw(self):
        group = pygame.sprite.GroupSingle()
        group.add(self)
        group.draw(self.display_surface)

    def move_left(self):
        self.rect.x -= self.vel

    def move_right(self):
        self.rect.x += self.vel

    def jump(self):
        self.rect.y -= 10
