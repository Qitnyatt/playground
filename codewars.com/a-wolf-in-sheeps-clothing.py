# https://www.codewars.com/kata/a-wolf-in-sheeps-clothing/train/python


def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    n = len(queue[queue.index('wolf') + 1:])
    return 'Oi! ' \
           'Sheep number {n}! ' \
           'You are about to be eaten by a wolf!'.format(n=n)
