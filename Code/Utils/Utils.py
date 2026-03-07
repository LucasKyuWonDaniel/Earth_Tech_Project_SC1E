from .classes import *
import pygame

# fonction pour faire apparaitre les element (platforme, boutton, fond, etc ...)
def draw_element(screen, element): # element -> list d'objet de la class ObjetClass
    screen.fill((30, 30, 30))
    for el in element:
        if el.visible:
            if el.type == "background":
                if len(el.frame) > 0:
                    screen.blit(el.frame[0], (0, 0))
            elif len(el.frame) == 0:
                pygame.draw.rect(screen, el.color, el.rect)
            elif len(el.frame) == 1:
                screen.blit(el.frame[0], el.rect.topleft)
            else:
                screen.blit(el.frame[int(el.anim_index) % len(el.frame)], el.rect.topleft)
                el.anim_index += el.anim_speed

# fonction qui cree une list d'element de la class ObjetClass et qui les renvoie dans une list
def create_element(element, niveau = 0, bg = '0'): # element = {"water" : [[160, 380, 50, 50]], "wall" : [[0, 70, 140, 3], [-1, 0, 1, 72]]}
    rect = []

    rect.append(ObjetClass('', 'background'))
    if bg != '0':
        rect[0].frame = [pygame.transform.scale(pygame.image.load("./Textures/" + bg).convert(), (1280, 720))]

    for key, val in element.items():
        for i in val:
            rect.append(ObjetClass(pygame.Rect(i[0]*10, i[1]*10, i[2]*10, i[3]*10), key))

            if key == "platform":
                if niveau == 1:
                    p_img = 'ciel_platform.png'
                else:
                    p_img = 'forest_platform.png'
                rect[-1].frame = [pygame.transform.scale(pygame.image.load("./Textures/maps/" + p_img).convert_alpha(),(120, 20))]
            elif key == "water":
                rect[-1].color = (0, 0, 255)

    return rect


