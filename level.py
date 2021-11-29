from types import SimpleNamespace
import pygame
from player import Player
from settings import WIDTH, tile_size, player_velocity
from tiles import Tile

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for tile_index, tile in enumerate(row):
                if tile == 'X':
                    x = tile_index * tile_size
                    y = row_index * tile_size
                    cell = Tile((x, y), tile_size)
                    self.tiles.add(cell)
                if tile == 'P':
                    x = tile_index * tile_size
                    y = row_index * tile_size
                    self.player = Player((x, y),tile_size, player_velocity, self.display_surface)
                    self.player_group.add(self.player)


    def scroll_map(self):
        direction = self.player.direction.x

        if self.player.rect.x < WIDTH / 4 and direction < 0:
            self.world_shift = player_velocity
            self.player.vel = 0

        elif self.player.rect.x > WIDTH - WIDTH / 4 and direction > 0:
            self.world_shift = -player_velocity
            self.player.vel = 0
        
        else:
            self.world_shift = 0
            self.player.vel = player_velocity

        self.tiles.update(self.world_shift)

    def horizontal_collision_movement(self):
        self.player.rect.x += self.player.vel * self.player.direction.x

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(self.player.rect):
                if self.player.direction.x < 0:
                    self.player.rect.left = sprite.rect.right
                if self.player.direction.x > 0:
                    self.player.rect.right = sprite.rect.left

    def vertical_collision_movement(self):
        self.player.handle_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0:
                    self.player.rect.bottom = sprite.rect.top
                    self.player.direction.y = 0
                    self.player.is_on_ground = True
                if self.player.direction.y < 0:
                    self.player.rect.top = sprite.rect.bottom
                    self.player.direction.y = 0
        

    def draw_level(self):
        self.scroll_map()
        self.tiles.draw(self.display_surface)

        self.player_group.draw(self.display_surface)
        self.player.update_player()
        self.horizontal_collision_movement()
        self.vertical_collision_movement()
