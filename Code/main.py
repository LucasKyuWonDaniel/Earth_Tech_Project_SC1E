import pygame
# Variables
x = 0
vx = 10
y = 670
vy = 10
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x,y,50,50))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        x -= vx
    if keys[pygame.K_d]:
        x += vx
    pygame.display.flip()
    clock.tick(60)

pygame.quit()