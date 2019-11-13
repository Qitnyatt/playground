# https://www.codewars.com/kata/new-cashier-does-not-know-about-space-or-shift/train/python


import re
import collections


def get_order(order):
    menu = [
        'Burger',
        'Fries',
        'Chicken',
        'Pizza',
        'Sandwich',
        'Onionrings',
        'Milkshake',
        'Coke',
    ]
    regex = r'|'.join(fr'({x.lower()})' for x in menu)
    matches = re.finditer(regex, order)
    result = collections.Counter()
    for match in matches:
        result.update({match.group().capitalize()})
    return ''.join(f' {x}' * result[x] for x in menu if result[x])[1:]
