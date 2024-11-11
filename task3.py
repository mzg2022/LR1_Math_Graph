import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

# Исходные координаты отрезка
segment = np.array([[100, 200], [300, 400]])

# Матрица преобразования
T = np.array([[1, 3], [4, 1]])

# Преобразование
new_segment = T @ segment.T

# Отображение
pygame.draw.line(screen, (255, 0, 0), (segment[0][0], segment[0][1]), (segment[1][0], segment[1][1]), 3)
pygame.draw.line(screen, (0, 0, 255), (new_segment[0][0], new_segment[1][0]), (new_segment[0][1], new_segment[1][1]), 3)

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
