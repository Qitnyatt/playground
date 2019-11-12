# https://www.codewars.com/kata/youre-a-square/train/python


import math


def is_square(n):
    if n < 0.0:
        return False
    fractional_part, _ = math.modf(n ** 0.5)
    if fractional_part:
        return False
    return True
