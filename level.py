import pygame
from settings import tile_size
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

    def draw_level(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
