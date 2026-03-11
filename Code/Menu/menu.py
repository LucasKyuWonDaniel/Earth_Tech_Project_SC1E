from .parametre_menu import*
from .niveau_menu import*
from .main_menu import*
from Code.Utils.Utils import draw_botton

# fonction qui permet de faire tourner les menu
def run_menu(screen, element, niveau, click, continue_click):
    screen.blit(element[0], (0, 0))
    screen.blit(element[1][0], element[1][1])
    niveau = draw_botton(screen, element[2:], click, niveau, continue_click)
    return niveau


# fonction qui permet d'initialiser les menu
def init_menu(menu, police):
    element = []
    if menu == -2:
        element = init_main_menu(police)
    elif menu == -1:
        element = init_lvl_menu(police)
    elif menu == -3:
        element = init_par_menu(police)

    return element