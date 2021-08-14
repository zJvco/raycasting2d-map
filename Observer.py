import pygame, math
from Ray import Ray


class Observer:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)
        self.rays = []
        for a in range(0, 360, 10):
            self.rays.append(Ray(x, y, 0, 0, a, 2000, color))

    def set_x(self, value):
        self.rect.x = value - self.size / 2

    def set_y(self, value):
        self.rect.y = value - self.size / 2

    def update(self, window, tiles):
        for ray in self.rays:
            ray.set_x(self.rect.x + self.size / 2)
            ray.set_y(self.rect.y + self.size / 2)
            ray.set_dir_x()
            ray.set_dir_y()

            dist_tl_record = math.inf
            pt_closest = None
            for tile in tiles:
                # Deixar o bloco alinhado no seu eixo.
                tx = tile.x + tile.size / 2
                ty = tile.y + tile.size / 2

                # Posição do observador no seu eixo.
                ox = self.rect.x + self.size / 2
                oy = self.rect.y + self.size / 2

                # Pontos de todas as vertices do retângulo
                px1 = tile.x
                py1 = tile.y
                px2 = tile.x
                py2 = tile.y + tile.size
                px3 = tile.x + tile.size
                py3 = tile.y + tile.size
                px4 = tile.x + tile.size
                py4 = tile.y

                dt = ray.calc_distance(tx, ty, ox, oy)

                vertex = [ray.cast(px1, py1, px2, py2), ray.cast(px2, py2, px3, py3), ray.cast(px3, py3, px4, py4), ray.cast(px4, py4, px1, py1)]
                dist_vt_record = math.inf
                vt_closest = None
                for pt in vertex:
                    if pt:
                        dv = ray.calc_distance(pt[0], pt[1], ox, oy)
                        if dv < dist_vt_record:
                            vt_closest = pt
                        dist_vt_record = min(dv, dist_vt_record)

                if vt_closest:
                    if dt < dist_tl_record:
                        pt_closest = vt_closest

                    dist_tl_record = min(dt, dist_tl_record)

            if pt_closest:
                ray.draw(window, pt_closest[0], pt_closest[1])

    def draw(self, window):
        pygame.draw.ellipse(window, self.color, self.rect)