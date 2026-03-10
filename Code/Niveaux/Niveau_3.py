import pygame
import random
from Code.Utils.Utils import *
from Code.Utils.classes import ObjetClass

def element_lvl_3():
    element = {
        "platform": [
            [0, 70, 130, 1],
            [20, 55, 15, 1],
            [50, 45, 15, 1],
            [80, 35, 15, 1],
            [110, 25, 15, 1],
        ],
        "wall": [
            [0, 0, 1, 72],
            [129, 0, 1, 72],
            [-1, 0, 1, 72]
        ],
        "poubelle_plastique": [
            [10, 65, 4, 5]
        ],
        "poubelle_verre": [
            [60, 65, 4, 5]
        ],
        "poubelle_papier": [
            [110, 65, 4, 5]
        ]
    }
    return element

def init_lvl_3(map):
    map.water = 0
    map.score = 0
    map.score_max = 20
    map.temps_restant = 60 * 60
    map.pollution = 0
    map.dechets = []
    map.dechet_transporte = None
    map.timer_apparition = 0
    map.intervalle_apparition = 120
    map.types_dechets = ["plastique", "verre", "papier"]
    map.couleurs_dechets = {
        "plastique": (255,255,0),
        "verre": (0,255,0),
        "papier": (0,0,255)
    }
    map.poubelles = []
    for e in map.element:
        if e.type in ["poubelle_plastique", "poubelle_verre", "poubelle_papier"]:
            map.poubelles.append(e)
            if e.type == "poubelle_plastique":
                e.type_dechet = "plastique"
                e.color = (255,255,0)
            elif e.type == "poubelle_verre":
                e.type_dechet = "verre"
                e.color = (0, 255, 0)
            elif e.type == "poubelle_papier":
                e.type_dechet = "papier"
                e.color = (0, 0, 255)

def utilisation_lvl_3(map, e):
    if map.dechet_transporte:
        if e.type in ["poubelle_plastique", "poubelle_verre", "poubelle_papier"]:
            if e.type_dechet == map.dechet_transporte["type"]:
                map.dechet_transporte = None
                map.score += 1
                map.pollution = max(0, map.pollution - 5)
            else:
                map.pollution = min(100, map.pollution + 5)
                map.dechet_transporte = None
            map.interaction = True
    elif e.type == "dechet" and not map.dechet_transporte:
        map.dechet_transporte = {
            "type": e.type_dechet,
            "couleur": e.color,
            "rect": e.rect
        }
        e.visible = False
        map.dechets.remove(e)
        map.interaction = True

def generer_dechet(map):
    if len(map.dechets) < 10:
        type_dechet = random.choice(map.types_dechets)
        couleur = map.couleurs_dechets[type_dechet]

        plateformes = [p for p in map.element if p.type == "platform"]
        if plateformes :
            p = random.choice(plateformes)
            x = p.rect.x + random.randint(10, p.rect.width - 30)
            y = p.rect.y - 20
            dechet = ObjetClass(pygame.Rect(x, y, 20, 20), "dechet")
            dechet.type_dechet = type_dechet
            dechet.color = couleur
            dechet.visible = True
            map.dechets.append(dechet)