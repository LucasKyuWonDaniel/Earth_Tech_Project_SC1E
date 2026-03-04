import pygame

pygame.init()
screen = pygame.display.set_mode((1240, 700))
clock = pygame.time.Clock()

joueur = pygame.Rect(100, 100, 40, 40)
vy = 0
gravite = 0.8
vx = 0
acceleration = 0.8
friction = 0.7
vitesse_max = 7

plateformes = [
    pygame.Rect(50, 500, 700, 30),  # Le sol
    pygame.Rect(150, 400, 200, 20), # Plateforme 1
    pygame.Rect(450, 300, 200, 20), # Plateforme 2
]

run = True
while run:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

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
    joueur.x += vx

    # Physique verticale
    vy += gravite
    joueur.y += vy

    # Détection de collision
    en_contact = False
    for p in plateformes:
        if joueur.colliderect(p):
            if vy > 0 and not keys[pygame.K_DOWN]:
                if (joueur.bottom - vy) <= p.top:
                    joueur.bottom = p.top
                    vy = 0
                    en_contact = True


            elif vy < 0:
                if joueur.top >= p.bottom + vy - 1:
                    joueur.top = p.bottom
                    vy = 0

    # Saut
    if keys[pygame.K_SPACE] and en_contact:
        vy = -16

    # Dessin
    pygame.draw.rect(screen, (0, 255, 100), joueur) # Joueur
    for p in plateformes:
        pygame.draw.rect(screen, (200, 200, 200), p) # Plateformes

    pygame.display.flip()
    clock.tick(60)

pygame.quit()