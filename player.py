from os import get_terminal_size
import pygame
from pygame import display
from pygame import key

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, velocity, display):
        super().__init__()
        self.display_surface = display
        self.image = pygame.Surface((size, size))
        self.image.fill('purple')
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0,0)
        self.vel = velocity
        self.gravity = 0.8
        self.jump_force = -15

    def handle_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def controller(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.vel
            self.direction.x = -1

        elif keys[pygame.K_d]:
            self.rect.x += self.vel
            self.direction.x = 1

        else: self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def jump(self):
        self.direction.y = self.jump_force

    def update_player(self):
        self.controller()
        self.handle_gravity()