import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

L = np.array([[-0.5, 1.5], [3, -2], [-1, -1], [3, 5/3]]) * 100
T = np.array([[1, 2], [1, -3]])
new_L = (T @ L.T).T + np.array([400, 300])

# Отображение отрезков
for i in range(0, 4, 2):
    pygame.draw.line(screen, (255, 0, 0), (L[i][0] + 400, -L[i][1] + 300), (L[i+1][0] + 400, -L[i+1][1] + 300), 3)
    pygame.draw.line(screen, (0, 0, 255), (new_L[i][0], -new_L[i][1]), (new_L[i+1][0], -new_L[i+1][1]), 3)

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
