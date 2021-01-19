point = (0.4, 0.5)
#         x    y

print(point)

from collections import namedtuple

Point2D = namedtuple("Point2D", ['x', 'y'])

p0 = Point2D(0.5, 0.6)

print(p0, p0)


def norme(p):
    d2 = p[0]**2 + p[1]**2
    return d2**0.5


point1 = (0, 0)
point2 = (1, 1)

print(norme(point))
print(norme(point1))
print(norme(point2))

p0 = Point2D(1, 1)
print(p0[0], p0[1])
print(p0.x, p0.y)

print(norme(p0))

p1 = Point2D(0, 1)

print(f"{p0} + {p1} = {p0+p1}")

p3 = Point2D(1, 2)


def ajout_point(p_1, p_2):
    p3_x = p_1[0] + p_2[0]
    p3_y = p_1[1] + p_2[1]
    return Point2D(p3_x, p3_y)


def ajout_point_nom(p_1, p_2):
    p3_x = p_1.x + p_2.y
    p3_y = p_1.x + p_2.y
    return Point2D(p3_x, p3_y)


print(f"{p0} + {p1} = {ajout_point(p0,p1)}")

print(f"Ajout ok = {ajout_point(p0,p1) == p3}")

print(f"Ajout ok nom = {ajout_point_nom(p0,p1) == p3}")

print(list(zip(p0, p1)))


def ajout_point_zip(p_1, p_2):
    coord = []
    for x in zip(p_1, p_2):
        print('coordonée')
        coord.append(sum(x))
        print(coord)
    return Point2D(coord[0], coord[1])


print(f"zip ok : {ajout_point_zip(p0, p1) == p3} ")

# Grouper les fonctions pas dimension ?
print("affichage points")

class ObjectPoint1D:
  def __init__(self, x):
    self.x = x

  def __str__(self):
    return f"Point1D(x={point1d.x})"

  def norm(self):
    return (self.x**2)**0.5



print(p3)

np1d = ObjectPoint1D(0.5)
np1d.x 
print(np1d)
print(np1d.norme())

np1d1 = ObjectPoint1D(0.6)
np1d1.x 
print(np1d)

