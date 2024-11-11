#graphics.py
import pygame
import numpy as np
import math as m


class Origin:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Unit:
    def __init__(self, length):
        self.length = length


class ReferenceFrame:
    def __init__(self, origin: Origin, unit: Unit):
        self.origin = origin
        self.unit = unit

    def get_x(self, x):
        return int(self.origin.x + x * self.unit.length)

    def get_y(self, y):
        return int(self.origin.y - y * self.unit.length)

    def get_length(self, dl):
        return int(dl * self.unit.length)


class Drawer:
    def __init__(self, res_x, res_y, color_depth, rf: ReferenceFrame):
        self.res_x = res_x
        self.res_y = res_y
        self.color_depth = color_depth
        self.rf = rf
        self.__color = (0, 0, 0)

    def initialize(self, caption: str):
        pygame.init()
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))
        pygame.display.set_caption(caption)
        self.screen.fill((255, 255, 255))

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def draw_text(self, x, y, text):
        font = pygame.font.SysFont(None, 24)
        img = font.render(text, True, self.__color)
        self.screen.blit(img, (self.rf.get_x(x), self.rf.get_y(y)))

    def draw_line(self, x1, y1, x2, y2, width=1):
        pygame.draw.line(self.screen, self.__color, (self.rf.get_x(x1), self.rf.get_y(y1)),
                         (self.rf.get_x(x2), self.rf.get_y(y2)), width)

    def draw_polygon(self, points, width=1):
        transformed_points = [(self.rf.get_x(p[0]), self.rf.get_y(p[1])) for p in points]
        pygame.draw.polygon(self.screen, self.__color, transformed_points, width)

    def draw_axes(self, x_min, x_max, y_min, y_max):
        self.draw_line(x_min, 0, x_max, 0, 1)
        self.draw_line(0, y_min, 0, y_max, 1)
