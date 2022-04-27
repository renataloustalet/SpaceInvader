import pygame

pygame.init()

# crea la pantalla
screen = pygame.display.set_mode((800, 600))

# Icono y titulo
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# jugador
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480


def player(x, y) :
    screen.blit(playerImg, (x, y))

running = True

while running:
    #RGB
    screen.fill((0, 0, 0))
    playerY -= 0.1

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    player(playerX, playerY)
    pygame.display.update()