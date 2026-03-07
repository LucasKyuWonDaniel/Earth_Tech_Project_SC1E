from .Utils import*
from .classes import*

# fontion pour gerer les colisions avec les objets
def collision(map, p):
    if (map.joueur.rect.colliderect(p.rect) and (p.type == "wall" or p.type == "platform")) or (p.rect.top - 1 <= map.joueur.rect.bottom <= p.rect.top + 1 and p.rect.left <= map.joueur.rect.right and map.joueur.rect.left <= p.rect.right):
        #vertical
        if map.vy > 0 and (map.joueur.rect.bottom - map.vy) <= p.rect.top:
            map.joueur.rect.bottom = p.rect.top
            map.vy = 0
            map.en_contact = True
        elif map.vy < 0 and map.joueur.rect.top >= p.rect.bottom + map.vy - 1:
            map.joueur.rect.top = p.rect.bottom
            map.vy = 0

        # horizontal
        elif map.joueur.rect.left < p.rect.right and (abs(map.joueur.rect.left - p.rect.right) < 15):
            map.joueur.rect.left = p.rect.right
        elif map.joueur.rect.right > p.rect.left and (abs(map.joueur.rect.right - p.rect.left) < 15):
             map.joueur.rect.right = p.rect.left

# Fonction pour gérer les interaction/utilisation avec la touche E
def utilisation(map, p):
    if map.joueur.rect.colliderect(p.rect) and p.type == "water" and map.niveau != 3 and map.water < 100:
        map.water += 2
        if map.water > 100:
            map.water = 100
        h = 120 * (map.water/100)
        map.water_tank.rect.height = h
        map.water_tank.rect.y = 660 - h

    # utilisation_lvl_1(map)
    # utilisation_lvl_2(map)
    # utilisation_lvl_4(map)

# Fonction qui rassemble la gest des colision et les interaction pour eviter des boucle similaire
def interaction(map):
    map.en_contact = False
    for p in map.element[1:]:
        collision(map, p)
        if map.keys[pygame.K_e]:
            utilisation(map, p)

# fonction pour gerer touts les mouvements du joueur
def mouvement(map):
    # changement de coordoné
    map.joueur.rect.y += map.vy
    map.joueur.rect.x += map.vx

    # Mouvement horizontal
    map.direction = 0

    if map.keys[pygame.K_LEFT] or map.keys[pygame.K_q]:
        map.direction = -1
    if map.keys[pygame.K_RIGHT] or map.keys[pygame.K_d]:
        map.direction += 1

    if map.direction != 0:
        map.vx += map.direction * map.acceleration
    else:
        map.vx *= map.friction

    if map.vx > map.vitesse_max:
        map.vx = map.vitesse_max
    if map.vx < -map.vitesse_max:
        map.vx = -map.vitesse_max
    if abs(map.vx) < 0.1:
        map.vx = 0

    # Physique verticale
    map.vy += map.gravite

    # Saut
    if (map.keys[pygame.K_SPACE] or map.keys[pygame.K_UP]) and map.en_contact:
        map.vy = -14

# fonction qui permet de faire tourner la map
def run_map(map, lvl_element = []):
    map.keys = pygame.key.get_pressed()

    mouvement(map)
    interaction(map)

    if map.direction != 0:
        map.d_save = map.direction
    else:
        map.joueur.anim_index = 0.0

    map.joueur.frame = map.player_img[map.d_save][map.en_contact]
    draw_element(map.screen, map.element + [map.joueur, map.water_tank] + lvl_element)



# fonction pour initialiser la map
def init_map(niveau, element, screen):
    joueur = ObjetClass(pygame.Rect(160, 380, 50, 50), "player")
    map = MapClass(0.7, 7, 0.8, 0.8, screen, joueur)
    map.vx = 0
    map.vy = 0
    map.direction = 0
    map.d_save = 1
    map.niveau = niveau
    if niveau == 1:
        map.element = create_element(element, niveau, "maps/ciel_background.png")
    else:
        map.element = create_element(element, niveau, "maps/forest_background.png")

    map.joueur.anim_speed = 0.2
    map.player_img[1][True] = [
        pygame.transform.scale(pygame.image.load("./Textures/player/player_right_1.png"), (50, 50)),
        pygame.transform.scale(pygame.image.load("./Textures/player/player_right_2.png"), (50, 50)),
        pygame.transform.scale(pygame.image.load("./Textures/player/player_right_3.png"), (50, 50)),
        pygame.transform.scale(pygame.image.load("./Textures/player/player_right_4.png"), (50, 50))
    ]
    map.player_img[-1][True] = [
        pygame.transform.scale(pygame.image.load("./Textures/player/player_left_1.png"), (50, 50)),
        pygame.transform.scale(pygame.image.load("./Textures/player/player_left_2.png"), (50, 50)),
        pygame.transform.scale(pygame.image.load("./Textures/player/player_left_3.png"), (50, 50)),
        pygame.transform.scale(pygame.image.load("./Textures/player/player_left_4.png"), (50, 50))
    ]

    map.player_img[1][False] = [pygame.transform.scale(pygame.image.load("./Textures/player/player_right_jump.png"), (50, 50))]
    map.player_img[-1][False] = [pygame.transform.scale(pygame.image.load("./Textures/player/player_left_jump.png"), (50, 50))]

    map.water_tank = ObjetClass(pygame.Rect(100, 540, 90, 0), "water_tank")
    map.water_tank.color = (50, 150, 255)
    if niveau == 3:
        map.water_tank.visible = False

    return map