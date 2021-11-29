import pygame
from player import Player
from settings import WIDTH, tile_size
from tiles import Tile

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
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
                    self.player = Player((x, y),tile_size, 8, self.display_surface)
                    self.tiles.add(self.player)


    def scroll_map(self):
        direction = self.player.direction.x

        if self.player.rect.x < WIDTH / 4 and direction < 0:
            self.world_shift = 8
            self.player.vel = 0

        elif self.player.rect.x > WIDTH - WIDTH / 4 and direction > 0:
            self.world_shift = -8
            self.player.vel = 0
        
        else:
            self.world_shift = 0
            self.player.vel = 8

        self.tiles.update(self.world_shift)

    def draw_level(self):
        self.scroll_map()
        self.player.update_player()
        self.tiles.draw(self.display_surface)
