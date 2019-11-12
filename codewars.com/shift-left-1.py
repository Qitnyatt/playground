# https://www.codewars.com/kata/shift-left-1/train/python


def shift_left(a, b):
    a, b = list(a), list(b)
    counter = 0

    while a != b:
        if len(a) > len(b):
            a.pop(0)
            counter += 1
        elif len(b) > len(a):
            b.pop(0)
            counter += 1
        else:
            a.pop(0)
            counter += 1
            b.pop(0)
            counter += 1

    return counter
