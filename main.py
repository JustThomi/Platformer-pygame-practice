import pygame
from level import Level
from settings import *

pygame.init()
pygame.display.set_caption("Platformer")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
level = Level(level_map, WIN)


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
