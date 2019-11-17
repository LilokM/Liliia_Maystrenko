import math
def distance(x1, y1, x2, y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return round(dist, 2)