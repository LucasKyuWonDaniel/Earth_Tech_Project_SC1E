import pygame
from Utils.Utils import*

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
    {"rect":pygame.Rect(50, 500, 700, 30),"type":"wall"},  # Le sol
    {"rect":pygame.Rect(150, 400, 200, 20),"type":"platform"}, # Plateforme 1
    {"rect":pygame.Rect(450, 300, 200, 20),"type":"platform"}, # Plateforme 2
]

run = True
while run:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    vx, vy = Mouvement(gravite, plateformes, friction, vitesse_max, joueur, acceleration, vx, vy)

    draw_element(screen, plateformes, joueur)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()