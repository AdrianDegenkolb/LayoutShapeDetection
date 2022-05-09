import math

import numpy


class Polygon:
    vertices: [[int]]
    middle: [int]

    def __init__(self, vertices, middle):
        self.vertices = vertices
        self.middle = middle

    def isCircle(self):
        minDist = float('inf')
        maxDist = 0
        for v in self.vertices:
            dx, dy = numpy.subtract(v - self.middle)
            dist = math.sqrt(pow(dx, 2) + pow(dy, 2))
            if dist < minDist:
                minDist = dist

            if dist > maxDist:
                maxDist = dist

        if minDist / maxDist > 0.9:
            return True
        else:
            return False

