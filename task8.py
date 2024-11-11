import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

L = np.array([[8, 1], [7, 3], [6, 2]]) * 100
T = np.array([[0, 1], [1, 0]])
new_L = (T @ L.T).T + np.array([400, 300])

pygame.draw.polygon(screen, (255, 0, 0), [(p[0] + 400, -p[1] + 300) for p in L])
pygame.draw.polygon(screen, (0, 0, 255), [(p[0], -p[1]) for p in new_L])

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
