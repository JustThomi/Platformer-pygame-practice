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
        self.direction = pygame.math.Vector2(0,0)
        self.vel = velocity

    def controller(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.vel
            self.direction.x = -1

        elif keys[pygame.K_d]:
            self.rect.x += self.vel
            self.direction.x = 1

        else: self.direction.x = 0
