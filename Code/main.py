from Utils.map import*
from Menu.menu import*
import pygame

# structure pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
police = None
click = False
continue_click = False

# premier initialisation
niveau = -2
if niveau > 0:
    if niveau == 1:
        element_lvl = element_lvl_1()
    elif niveau == 2:
        element_lvl = {}
    elif niveau == 3:
        element_lvl = element_lvl_3()
    else:
        element_lvl = element_lvl_1()

    element = element_map_general() | element_lvl
    map = init_map(niveau, screen)
else:
    element = init_menu(niveau, police)


# Boucle principale de Pygame
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click = True
        else:
            click = False

    # run menu ou niveau
    if niveau > 0 :
        map.click = click
        run_map(map)
        new_niveau = map.niveau
    else:
        new_niveau = run_menu(screen, element, niveau, click, continue_click)

    # initialisation de la map ou niveau lors d'un changement
    if niveau != new_niveau:
        niveau = new_niveau
        if niveau > 0:
            map = init_map(niveau, screen)
        elif niveau == 0:
            run = False
        else:
            element = init_menu(niveau, police)

    continue_click = click
    pygame.display.flip()
    clock.tick(60)

pygame.quit()