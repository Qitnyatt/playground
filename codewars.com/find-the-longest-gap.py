# https://www.codewars.com/kata/find-the-longest-gap/train/python


def gap(num):
    x = bin(num)[2:].replace('1', '##').split('#')
    while x and x[-1] != '':
        x.pop()
    return len(max(x))
