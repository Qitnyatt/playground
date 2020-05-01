# https://www.codewars.com/kata/easy-wallpaper/train/python


import math


def wallpaper(l, w, h):
    if l <= 0 or w <= 0 or h <= 0:
        return 'zero'
    length_roll = 10.0
    width_roll = 0.52
    reserve_fund_percent = 0.15
    walls_area = (l * h) * 2 + (w * h) * 2
    roll_area = length_roll * width_roll
    need_rolls = (walls_area / roll_area) * (1 + reserve_fund_percent)
    return [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen',
        'twenty',
    ][math.ceil(need_rolls)]
