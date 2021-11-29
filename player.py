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

        self.is_on_ground = False
        self.direction = pygame.math.Vector2(0,0)
        self.vel = velocity
        self.gravity = 0.9
        self.jump_force = -20

    def handle_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def controller(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -1

        elif keys[pygame.K_d]:
            self.direction.x = 1

        else: self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.is_on_ground:
                self.jump()

    def jump(self):
        self.direction.y = self.jump_force
        self.is_on_ground = False

    def update_player(self):
        self.controller()