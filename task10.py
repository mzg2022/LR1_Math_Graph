import math
import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

a, b = 1, 5
theta = 0

while theta < 4 * math.pi:
    r = b + 2 * a * math.cos(theta)
    x = int(400 + r * math.cos(theta))
    y = int(300 - r * math.sin(theta))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 2)
    theta += 0.1

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
