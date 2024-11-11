import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
# Инициализация
L = np.array([[50, 100], [250, 200], [50, 200], [250, 300]])
T = np.array([[1, 2], [3, 1]])
new_L = (T @ L.T).T

# Функция расчета наклона
def calculate_slope(point1, point2):
    return (point2[1] - point1[1]) / (point2[0] - point1[0])

# Расчет начальных и конечных наклонов
original_slope1 = calculate_slope(L[0], L[1])
original_slope2 = calculate_slope(L[2], L[3])
transformed_slope1 = calculate_slope(new_L[0], new_L[1])
transformed_slope2 = calculate_slope(new_L[2], new_L[3])

# Отображение отрезков
for i in range(0, 4, 2):
    pygame.draw.line(screen, (255, 0, 0), (L[i][0] + 400, -L[i][1] + 300), (L[i+1][0] + 400, -L[i+1][1] + 300), 3)
    pygame.draw.line(screen, (0, 0, 255), (new_L[i][0] + 400, -new_L[i][1] + 300), (new_L[i+1][0] + 400, -new_L[i+1][1] + 300), 3)

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
