from Utils.Utils import*
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()

joueur = pygame.Rect(160, 380, 50, 50)
vy = 0
vx = 0
anim_index = 0.0
gravite = 0.8
d_save = 1
acceleration = 0.8
friction = 0.7
vitesse_max = 7

element = {
    "wall" : [
        [0, 70, 130, 3],
        [-1, 0, 1, 72],
        [128, 0, 1, 72],
        [0, 45, 30, 25]
    ],
    "water" : [1,42,14,4],
    "platform" : [
        [89, 60], [45, 60], [67, 50], [60, 21], [107, 24], [48, 41], [25, 34], [6, 23], [33, 14], [78, 31], [96, 41]
    ]
}
hitbox = create_elements(element)

run = True
while run:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    vx, vy, en_contact, direction = mouvement(gravite, hitbox, friction, vitesse_max, joueur, acceleration, vx, vy)
    if direction != 0:
        d_save = direction
        anim_index += 0.3
    else:
        anim_index = 0.0

    draw_element(screen, hitbox, joueur, en_contact, direction, d_save, anim_index)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()