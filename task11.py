import pygame
import numpy as np

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

# Начальные координаты вершин квадрата
X = np.array([[2, -2], [-2, -2], [-2, 2], [2, 2]]) * 100

# Коэффициенты масштабирования и поворота
m = 0.9
alpha = np.pi / 32

# Матрицы преобразований
scale_matrix = np.array([[m, 0], [0, m]])
rotation_matrix = np.array([[np.cos(alpha), -np.sin(alpha)], [np.sin(alpha), np.cos(alpha)]])
transformation = scale_matrix @ rotation_matrix  # Комбинированная матрица преобразования

# Центр экрана
center = np.array([400, 300])

# Основной цикл отрисовки и преобразований
for _ in range(20):
    # Преобразуем координаты квадрата
    X = (transformation @ X.T).T

    # Смещаем квадрат к центру экрана
    transformed_X = X + center

    # Очищаем экран
    screen.fill((255, 255, 255))

    # Отображаем квадрат
    pygame.draw.polygon(screen, (255, 0, 0), [(int(p[0]), int(p[1])) for p in transformed_X], 1)

    # Обновляем экран
    pygame.display.flip()
    pygame.time.wait(200)

pygame.quit()
