# A pygame implementation of the space invaders game

import pygame
import random
import utils

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    dt = clock.tick(60) / 1000

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "white", player_pos, 40)
    for i in range(10):
        utils.Enemy(screen)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    if keys[pygame.K_SPACE]:
        lasers.append(utils.Laser(screen, (player_pos.x, player_pos.y), "red", dt))

    _ = list(map(lambda x: x.move(lasers), lasers))

    # end of render
    pygame.display.flip()

pygame.quit()
