# https://www.codewars.com/kata/area-of-a-square/train/python


import math


def square_area(a):
    if a == 0:
        return 0
    side = a / (2 * math.pi * (90 / 360))
    area = side * side
    return round(area, 2)
