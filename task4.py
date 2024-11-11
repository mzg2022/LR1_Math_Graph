import pygame
import numpy as np

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

# Исходные точки отрезка L
L = np.array([[0, 100], [200, 300]])

# Матрица преобразования
T = np.array([[1, 2], [3, 1]])

# Применение матричного преобразования к точкам
new_L = T @ L.T

# Вычисление середины отрезков
mid_original = np.mean(L, axis=0)
mid_transformed = np.mean(new_L.T, axis=0)

# Отображение отрезков и середины
pygame.draw.line(screen, (255, 0, 0), (L[0][0] + 400, -L[0][1] + 300), (L[1][0] + 400, -L[1][1] + 300), 3)
pygame.draw.line(screen, (0, 0, 255), (new_L[0][0] + 400, -new_L[1][0] + 300), (new_L[0][1] + 400, -new_L[1][1] + 300), 3)

# Отображение середины отрезков
pygame.draw.circle(screen, (0, 255, 0), (mid_original[0] + 400, -mid_original[1] + 300), 5)
pygame.draw.circle(screen, (255, 255, 0), (mid_transformed[0] + 400, -mid_transformed[1] + 300), 5)

# Соединение середин отрезков
pygame.draw.line(screen, (0, 0, 0), (mid_original[0] + 400, -mid_original[1] + 300), (mid_transformed[0] + 400, -mid_transformed[1] + 300), 1)

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
