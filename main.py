import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('fish.png')
pygame.display.set_icon(icon)
running = True
colors = [(128, 128, 128), (0, 128, 128), (192, 192, 192), (0, 0, 255), (0, 206, 209)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    color = random.choice(colors)
    screen.fill(color)
    pygame.display.update()
    time.sleep(0.3)
