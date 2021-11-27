import pygame
from level import Level
from player import Player
from settings import *

pygame.init()
pygame.display.set_caption("Platformer")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

level = Level(level_map, WIN)
player = Player((200, 200), tile_size, 10, WIN)

def controlls(keys):
    if keys[pygame.K_a]:
        player.move_left()

    if keys[pygame.K_d]:
        player.move_right()

    # if keys[pygame.K_LEFT]:
    #     level.world_shift = -10
    #     level.scroll_map()

    # if keys[pygame.K_RIGHT]:
    #     level.world_shift = 10
    #     level.scroll_map()

def draw():
    WIN.fill('black')
    level.draw_level()
    player.draw()
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        controlls(keys)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()


if __name__ == "__main__":
    main()
