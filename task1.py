import pygame
import numpy as np

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Point Transformation")
screen.fill((255, 255, 255))

# Исходные координаты
x, y = map(int, input("Введите координаты точки (через пробел): ").split())
point = np.array([x, y])

# Матрица преобразования
T = np.array([[1, 3], [4, 1]])

# Преобразование точки
new_point = T @ point

# Отображение точек
pygame.draw.circle(screen, (255, 0, 0), (x + 400, -y + 300), 5)       # Исходная точка
pygame.draw.circle(screen, (0, 0, 255), (new_point[0] + 400, -new_point[1] + 300), 5)  # Преобразованная точка

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
