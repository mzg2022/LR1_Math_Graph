# main.py

import pygame
import sys
import numpy as np
import math as m
from squares.graphics import Drawer, ReferenceFrame, Origin, Unit
from squares.transform import translate, scale, rotate
from pygame.locals import *

# Параметры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30

# Параметры квадрата
initial_square = np.array([
    [-3, -3, 1],  # Левый нижний угол
    [3, -3, 1],  # Правый нижний угол
    [3, 3, 1],  # Правый верхний угол
    [-3, 3, 1]  # Левый верхний угол
])

# Константы преобразования
ROTATION_ANGLE = m.pi / 64
SCALE_X = 0.95
SCALE_Y = 0.95

# Время для сохранения кадров
SAVE_INTERVAL = 100  # миллисекунд


def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Square Funnel")
    clock = pygame.time.Clock()

    origin = Origin(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)  # Центр окна
    unit = Unit(100)  # Длина единицы
    rf = ReferenceFrame(origin, unit)  # Система отсчета
    drawer = Drawer(WINDOW_WIDTH, WINDOW_HEIGHT, 32, rf)
    drawer.initialize("Square Funnel")
    drawer.color = (255, 255, 255)  # Белый цвет

    # Центр квадрата
    x_c, y_c = 0, 0  # центр квадрата теперь (0,0), так как мы перемещаем квадрат к нему

    # Запуск основного цикла
    square = initial_square.copy()

    # Инициализация переменных для сохранения кадров
    last_save_time = pygame.time.get_ticks()  # Начальное значение времени
    saved_frames = []  # Список для хранения сохраненных кадров

    while True:
        current_time = pygame.time.get_ticks()

        # Проверка времени для сохранения кадров
        if current_time - last_save_time >= SAVE_INTERVAL:
            # Сохранение текущего состояния квадрата
            saved_frames.append(square.copy())
            last_save_time = current_time  # Обновление времени последнего сохранения

        # Применение преобразований
        transform_matrix = (
                translate(-x_c, -y_c) @  # Перемещение в начало координат
                rotate(ROTATION_ANGLE) @  # Поворот
                scale(SCALE_X, SCALE_Y) @  # Масштабирование
                translate(x_c, y_c)  # Возврат в центр
        )
        square = square @ transform_matrix  # Применение преобразований

        # Очистка экрана
        screen.fill((0, 0, 0))  # Черный фон

        # Отрисовка сохраненных кадров
        drawer.color = (255, 0, 0)  # Красный цвет для сохраненных кадров
        for frame in saved_frames:
            drawer.draw_polygon(frame, 1)

        # Отрисовка текущего кадра
        drawer.color = (255, 255, 255)  # Белый цвет для текущего квадрата
        drawer.draw_polygon(square, 1)

        # Обновление экрана и задержка
        pygame.display.flip()
        clock.tick(FPS)

        # Основной цикл для удержания окна открытым
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()



