from math import pi


def compute_area(radius):
    '''Given a circle's radius, it computes the area'''

    if radius < 0:
        raise ValueError("Radius should be positive")

    if type(radius) not in [int, float]:
        raise TypeError("Radius should be a real number")

    return radius * radius * pi
