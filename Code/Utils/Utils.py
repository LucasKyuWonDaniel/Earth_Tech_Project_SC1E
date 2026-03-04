import pygame

def draw_element(screen, element, joueur):
    pygame.draw.rect(screen, (0, 255, 100), joueur) # joueur
    for p in element:
        pygame.draw.rect(screen, (200, 200, 200), p["rect"]) # Plateformes

def collision(joueur, plateformes, vy, vx):
    en_contact = False
    for p in plateformes:
        if joueur.colliderect(p["rect"]):
            if p["type"] == "wall" or p["type"] == "platform":
                if vy > 0:
                    if (joueur.bottom - vy) <= p["rect"].top:
                        joueur.bottom = p["rect"].top
                        vy = 0
                        en_contact = True

                    else:
                        if vx > 0:
                            joueur.right = p["rect"].left
                        elif vx < 0:
                            joueur.left = p["rect"].right
                        vx = 0

                elif vy < 0:
                    if joueur.top >= p["rect"].bottom + vy - 1:
                        joueur.top = p["rect"].bottom
                        vy = 0

    return en_contact, vy, vx

def Mouvement(gravite, plateformes, friction, vitesse_max, joueur, acceleration, vx, vy):
    # Mouvement horizontal
    keys = pygame.key.get_pressed()
    direction = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        direction = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction += 1

    if direction != 0:
        vx += direction * acceleration
    else:
        vx *= friction

    if vx > vitesse_max:
        vx = vitesse_max
    if vx < -vitesse_max:
        vx = -vitesse_max
    if abs(vx) < 0.1:
        vx = 0


    # Physique verticale
    vy += gravite

    en_contact, vy, vx = collision(joueur, plateformes, vy, vx)

    # changement de coordoné
    joueur.y += vy
    joueur.x += vx

    # Saut
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and en_contact:
        vy = -16

    return vx, vy

