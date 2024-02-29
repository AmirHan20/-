import pygame
import random

pygame.init()

display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Graphical game")

player = pygame.Rect(0, 550, 20, 20)
player_speed = 5

# Настройка цели
target = pygame.Rect(300, 50, 20, 20)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.y -= player_speed
            elif event.key == pygame.K_DOWN:
                player.y += player_speed
            elif event.key == pygame.K_LEFT:
                player.x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player.x += player_speed

    if player.colliderect(target):
        target.x = random.randint(0, 580)
        target.y = random.randint(0, 580)

    if player.x < 0:
        player.x = 0
    elif player.x > 580:
        player.x = 580
    if player.y < 0:
        player.y = 0
    elif player.y > 580:
        player.y = 580

    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 255, 255), player)
    pygame.draw.rect(display, (255, 0, 0), target)

    pygame.display.update()

pygame.quit()
