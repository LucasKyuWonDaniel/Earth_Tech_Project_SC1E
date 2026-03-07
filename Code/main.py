from Utils.map import*
import pygame

# structure pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# Initialisation de la position de chaque elements de la map
element = {
    "wall" : [
        [0, 70, 140, 3],
        [-1, 0, 1, 72],
        [128, 0, 1, 72],
        [0, 45, 30, 25]
    ],
    "water" : [[1,43,14,4]],
    "platform" : [
        [89, 60, 12, 2],
        [45, 60, 12, 2],
        [67, 50, 12, 2],
        [60, 21, 12, 2],
        [107, 24, 12, 2],
        [48, 41, 12, 2],
        [25, 34, 12, 2],
        [6, 23, 12, 2],
        [33, 14, 12, 2],
        [78, 31, 12, 2],
        [96, 41, 12, 2]
    ],
}
map = init_map(0, element, screen)


# Boucle principale de Pygame
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    run_map(map)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()