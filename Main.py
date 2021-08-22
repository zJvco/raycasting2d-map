import pygame, sys
from Observer import Observer
from Tile import Tile
from random import randint

pygame.init()
pygame.display.set_caption("RayCasting")

window_size = (1000, 800)
window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

fps = 60

WHITE_COLOR = (255, 255, 255)
GRAY_COLOR = (155, 155, 155)
RED_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)


def getRandomPosition(i, e):
    return randint(i, e)


tiles = []
tiles_length = 10
tile_size = 40
for i in range(20):
    for j in range(25):
        if 0 < i < 19:
            if j < 24:
                j = 0
        tiles.append(Tile(tile_size * j, tile_size * i, tile_size, RED_COLOR))

observer = Observer(0, 0, 25, WHITE_COLOR)

start = False

running = True
while running:
    window.fill(BLACK_COLOR)

    mx, my = pygame.mouse.get_pos()
    pl, pr = pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Iniciar
            if event.key == pygame.K_RETURN:
                start = True
            # Editar
            if event.key == pygame.K_f:
                start = False

    if start:
        observer.set_x(mx)
        observer.set_y(my)
        observer.update(window, tiles)
        observer.draw(window)
    else:
        if pl:
            tiles.append(Tile(mx - tile_size / 2, my - tile_size / 2, tile_size, RED_COLOR))

    for tile in tiles:
        tile.draw(window)

    pygame.display.flip()
    clock.tick(fps)