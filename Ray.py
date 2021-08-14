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

    def intersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
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

    def cast(self, window, t):
        # Tile point n1, n2 ... n
        px1 = t.x
        py1 = t.y
        px2 = t.x
        py2 = t.y + t.size
        px3 = t.x + t.size
        py3 = t.y + t.size
        px4 = t.x + t.size
        py4 = t.y

        # Ray points
        rx1 = self.x
        ry1 = self.y
        rx2 = self.dir_x
        ry2 = self.dir_y

        pts = [self.intersection(px1, py1, px2, py2, rx1, ry1, rx2, ry2), self.intersection(px2, py2, px3, py3, rx1, ry1, rx2, ry2), self.intersection(px3, py3, px4, py4, rx1, ry1, rx2, ry2), self.intersection(px4, py4, px1, py1, rx1, ry1, rx2, ry2)]

        return pts

    def draw(self, window, ptx, pty):
        pygame.draw.aaline(window, self.color, (self.x, self.y), (ptx, pty))