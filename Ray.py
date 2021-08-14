import pygame, math


class Ray:
    def __init__(self, x, y, dir_x, dir_y, angle, r, color):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.angle = angle
        self.r = r
        self.color = color

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    def set_dir_x(self):
        self.dir_x = self.x + self.r * math.cos(math.radians(self.angle))

    def set_dir_y(self):
        self.dir_y = self.y + self.r * math.sin(math.radians(self.angle))

    def calc_distance(self, x1, y1, x2, y2):
        # Calcular a distancia de um ponto ao ponto
        d = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return d

    def cast(self, x1, y1, x2, y2):
        # Ponto de origen e de direção do raio
        x3 = self.x
        y3 = self.y
        x4 = self.dir_x
        y4 = self.dir_y

        # Calcular a direção entre as duas retas (linhas), se for 0, elas são paralelas, ou seja, nunca iram se encontrar.
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return

        # 't' é a posição no eixo y / 'u' é a posição no eixo x
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if 0 < t < 1 and 0 < u < 1:
            ptx = x1 + t * (x2 - x1)
            pty = y1 + t * (y2 - y1)
            return ptx, pty
        else:
            return

    def draw(self, window, ptx, pty):
        pygame.draw.aaline(window, self.color, (self.x, self.y), (ptx, pty))